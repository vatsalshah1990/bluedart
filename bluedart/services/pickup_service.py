"""
Pickup Service Module
"""

from bluedart.base_service import BlueDartBaseService


class BlueDartPickupRequest(BlueDartBaseService):
    """
    This class allows you to process (create) a new BlueDart shipment.
    """

    def __init__(self, profile_obj, *args, **kwargs):

        self.profile_obj = profile_obj

        wsdl_url = "http://netconnect.bluedart.com/Ver1.7/ShippingAPI/Pickup/PickupRegistrationService.svc?wsdl"
        if self.profile_obj.use_test_server:
            wsdl_url = "http://netconnect.bluedart.com/Demo/ShippingAPI/Pickup/PickupRegistrationService.svc?wsdl"

        self.request = None
        self.profile = None

        super(BlueDartPickupRequest, self).__init__(wsdl_url, *args, **kwargs)

    def _set_profile(self):
        self.profile.Api_type = self.profile_obj.api_type
        self.profile.LoginID = self.profile_obj.login_id
        self.profile.LicenceKey = self.profile_obj.license_key
        self.profile.Version = self.profile_obj.version

    def _prepare_wsdl_objects(self):
        """
        This is the data that will be used to create your shipment. Create
        the data structure and get it ready for the WSDL request.
        """

        self.request = self.client.factory.create('ns2:PickupRegistrationRequest')
        self.profile = self.client.factory.create('ns0:UserProfile')

        self._set_profile()

    def _assemble_and_send_request(self):
        """
        Fires off the Bluedart request.

        @warning: NEVER CALL THIS METHOD DIRECTLY. CALL send_request(),
            WHICH RESIDES ON FedexBaseService AND IS INHERITED.
        """

        # Fire off the query.
        return self.client.service.RegisterPickup(self.request, self.profile)