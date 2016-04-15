"""
Ship Service Module
"""

from bluedart.base_service import BlueDartBaseService


class BlueDartProcessShipmentRequest(BlueDartBaseService):
    """
    This class allows you to process (create) a new BlueDart shipment.
    """

    def __init__(self, profile_obj, *args, **kwargs):

        self.profile = profile_obj

        wsdl_url = "http://netconnect.bluedart.com/Ver1.7/ShippingAPI/WayBill/WayBillGeneration.svc?wsdl"
        if self.profile.use_test_server:
            wsdl_url = "http://netconnect.bluedart.com/Demo/ShippingAPI/Waybill/WayBillGeneration.svc?wsdl"
        super(BlueDartProcessShipmentRequest, self).__init__(wsdl_url, *args, **kwargs)

    def _set_profile(self):
        self.GenerateWayBill.Profile.Api_type = self.profile.api_type
        self.GenerateWayBill.Profile.LoginID = self.profile.login_id
        self.GenerateWayBill.Profile.LicenceKey = self.profile.license_key
        self.GenerateWayBill.Profile.Version = self.profile.version

    def _prepare_wsdl_objects(self):
        """
        This is the data that will be used to create your shipment. Create
        the data structure and get it ready for the WSDL request.
        """
        self.GenerateWayBill = self.client.factory.create("GenerateWayBill")
        self.GenerateWayBill.Request = self.client.factory.create("WayBillGenerationRequest")
        self.GenerateWayBill.Profile = self.client.factory.create("UserProfile")

        self.GenerateWayBill.Request.Consignee = self.client.factory.create("Consignee")
        self.GenerateWayBill.Request.Shipper = self.client.factory.create("Shipper")

        self.GenerateWayBill.Request.Services = self.client.factory.create("Services")
        self.GenerateWayBill.Request.Services.Commodity = self.client.factory.create("CommodityDetail")
        self.GenerateWayBill.Request.Services.Dimensions = []

        self._set_profile()

        self.logger.debug(self.GenerateWayBill)

    def _assemble_and_send_request(self):
        """
        Fires off the Bluedart request.
        
        @warning: NEVER CALL THIS METHOD DIRECTLY. CALL send_request(), 
            WHICH RESIDES ON FedexBaseService AND IS INHERITED.
        """

        # Fire off the query.
        return self.client.service.GenerateWayBill(self.GenerateWayBill)
