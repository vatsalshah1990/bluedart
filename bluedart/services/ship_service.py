"""
Ship Service Module
"""

from bluedart.base_service import BlueDartBaseService


class BlueDartProcessShipmentRequest(BlueDartBaseService):
    """
    This class allows you to process (create) a new BlueDart shipment.
    """

    def __init__(self, profile_obj, *args, **kwargs):

        self.profile_obj = profile_obj

        wsdl_url = "http://netconnect.bluedart.com/Ver1.7/ShippingAPI/WayBill/WayBillGeneration.svc?wsdl"
        if self.profile_obj.use_test_server:
            wsdl_url = "http://netconnect.bluedart.com/Demo/ShippingAPI/Waybill/WayBillGeneration.svc?wsdl"

        self.Request = None
        self.Profile = None

        super(BlueDartProcessShipmentRequest, self).__init__(wsdl_url, *args, **kwargs)

    def _set_profile(self):
        self.Profile.Api_type = self.profile_obj.api_type
        self.Profile.LoginID = self.profile_obj.login_id
        self.Profile.LicenceKey = self.profile_obj.license_key
        self.Profile.Version = self.profile_obj.version

    def _prepare_wsdl_objects(self):
        """
        This is the data that will be used to create your shipment. Create
        the data structure and get it ready for the WSDL request.
        """

        self.Request = self.client.factory.create('ns2:WayBillGenerationRequest')
        self.Profile = self.client.factory.create('ns0:UserProfile')

        self.Request.Consignee = self.client.factory.create("ns2:Consignee")
        self.Request.Shipper = self.client.factory.create("ns2:Shipper")

        self.Request.Services = self.client.factory.create("ns2:Services")
        self.Request.Services.Commodity = self.client.factory.create("ns2:CommodityDetail")

        self._set_profile()

    def _assemble_and_send_request(self):
        """
        Fires off the Bluedart request.
        
        @warning: NEVER CALL THIS METHOD DIRECTLY. CALL send_request(), 
            WHICH RESIDES ON FedexBaseService AND IS INHERITED.
        """

        # Fire off the query.
        return self.client.service.GenerateWayBill(self.Request, self.Profile)


class BlueDartCancelShipmentRequest(BlueDartBaseService):
    """
    This class allows you to process (create) a new BlueDart shipment.
    """

    def __init__(self, profile_obj, *args, **kwargs):

        self.profile_obj = profile_obj

        wsdl_url = "http://netconnect.bluedart.com/Ver1.7/ShippingAPI/WayBill/WayBillGeneration.svc?wsdl"
        if self.profile_obj.use_test_server:
            wsdl_url = "http://netconnect.bluedart.com/Demo/ShippingAPI/Waybill/WayBillGeneration.svc?wsdl"

        self.Request = None
        self.Profile = None

        super(BlueDartCancelShipmentRequest, self).__init__(wsdl_url, *args, **kwargs)

    def _set_profile(self):
        self.Profile.Api_type = self.profile_obj.api_type
        self.Profile.LoginID = self.profile_obj.login_id
        self.Profile.LicenceKey = self.profile_obj.license_key
        self.Profile.Version = self.profile_obj.version

    def _prepare_wsdl_objects(self):
        """
        This is the data that will be used to create your shipment. Create
        the data structure and get it ready for the WSDL request.
        """

        self.Request = self.client.factory.create('ns2:AWBCancelationRequest')
        self.Profile = self.client.factory.create('ns0:UserProfile')

        self._set_profile()

    def _assemble_and_send_request(self):
        """
        Fires off the Bluedart request.

        @warning: NEVER CALL THIS METHOD DIRECTLY. CALL send_request(),
            WHICH RESIDES ON FedexBaseService AND IS INHERITED.
        """

        # Fire off the query.
        return self.client.service.GenerateWayBill(self.Request, self.Profile)
