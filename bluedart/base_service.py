import logging

import suds
from suds.client import Client
from suds.plugin import MessagePlugin


class GeneralSudsPlugin(MessagePlugin):
    """
    General Suds Plugin: Adds logging request and response functionality
    and prunes empty WSDL objects before sending.
    """

    def __init__(self, **kwargs):
        """Initializes the request and response loggers."""
        self.request_logger = logging.getLogger('bluedart.request')
        self.response_logger = logging.getLogger('bluedart.response')
        self.kwargs = kwargs

    def marshalled(self, context):
        """Removes the WSDL objects that do not have a value before sending."""
        context.envelope = context.envelope.prune()

    def sending(self, context):
        """Logs the sent request."""
        self.request_logger.info("BlueDart Request {}".format(context.envelope))

    def received(self, context):
        """Logs the received response."""
        self.response_logger.info("BlueDart Response {}".format(context.reply))


class BluedartBaseServiceException(Exception):
    """
    Exception: Serves as the base exception that other service-related
    exception objects are sub-classed from.
    """

    def __init__(self, error_code, value):
        self.error_code = error_code
        self.value = value

    def __unicode__(self):
        return "%s (Error code: %s)" % (repr(self.value), self.error_code)

    def __str__(self):
        return self.__unicode__()


class BluedartBaseServiceExceptionFailure(BluedartBaseServiceException):
    """
    Exception: The request could not be handled at this time. This is generally
    a server problem.
    """

    pass


class BluedartBaseServiceExceptionError(BluedartBaseServiceException):
    """
    Exception: These are generally problems with the client-provided data.
    """

    pass


class SchemaValidationError(BluedartBaseServiceException):
    """
    Exception: There is probably a problem in the data you provided.
    """

    def __init__(self, fault):
        self.error_code = -1
        self.value = "suds encountered an error validating your data against this service's WSDL schema. " \
                     "Please double-check for missing or invalid values, filling all required fields."
        try:
            self.value += ' Details: {}'.format(fault)
        except AttributeError:
            pass


class BlueDartBaseService(object):
    def __init__(self, wsdl_url, *args, **kwargs):

        self.logger = logging.getLogger('bluedart')
        """@ivar: Python logger instance with name 'bluedart'."""

        self.client = Client(wsdl_url, plugins=[GeneralSudsPlugin()])
        # self.client.options.cache.clear()  # Clear the cache, then re-init client when changing wsdl file.
        self._prepare_wsdl_objects()

    def _prepare_wsdl_objects(self):
        """
        This method should be over-ridden on each sub-class. It instantiates
        any of the required WSDL objects so the user can just print their
        __str__() methods and see what they need to fill in.
        """

        pass

    def __check_response_for_bluedart_error(self):
        """
        This checks the response for general bluedart errors that aren't related
        to any one WSDL.
        """

        pass

    def _check_response_for_request_errors(self):
        """
        Override this in each service module to check for errors that are
        specific to that module. For example, invalid tracking numbers in
        a Tracking request.
        """

        pass

    def _check_response_for_request_warnings(self):
        """
        Override this in a service module to check for errors that are
        specific to that module. For example, changing state/province based
        on postal code in a Rate Service request.
        """

        pass

    def create_wsdl_object_of_type(self, type_name):
        """
        Creates and returns a WSDL object of the specified type.
        :param type_name: specifies the object's type name from WSDL.
        """

        return self.client.factory.create(type_name)

    def _assemble_and_send_request(self):
        """
        This method should be over-ridden on each sub-class.
        It assembles all required objects
        into the specific request object and calls send_request.
        Objects that are not set will be pruned before sending
        via GeneralSudsPlugin marshalled function.
        """

        pass

    def send_request(self, send_function=None):
        """
        Sends the assembled request on the child object.
        @type send_function: function reference
        @keyword send_function: A function reference (passed without the
            parenthesis) to a function that will send the request. This
            allows for overriding the default function in cases such as
            validation requests.
        """

        # Send the request and get the response back.
        try:
            # If the user has overridden the send function, use theirs
            # instead of the default.
            if send_function:
                # Follow the overridden function.
                self.response = send_function()
            else:
                # Default scenario, business as usual.
                self.response = self._assemble_and_send_request()
        except suds.WebFault as fault:
            # When this happens, throw an informative message reminding the
            # user to check all required variables, making sure they are
            # populated and valid
            raise SchemaValidationError(fault.fault)

        # Check the response for general bluedart errors/failures that aren't
        # specific to any given WSDL/request.
        self.__check_response_for_bluedart_error()

        # Check the response for errors specific to the particular request.
        # This method can be overridden by a method on the child class object.
        self._check_response_for_request_errors()

        # Check the response for errors specific to the particular request.
        # This method can be overridden by a method on the child class object.
        self._check_response_for_request_warnings()

        # Debug output. (See Request and Response output)
        self.logger.debug("== bluedart QUERY RESULT ==")
        self.logger.debug(self.response)
