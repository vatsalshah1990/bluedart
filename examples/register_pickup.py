import logging

import sys

# Un-comment to see the response from Bluedart printed in stdout.
from bluedart.services.pickup_service import BlueDartPickupRequest
from examples.example_profile import PROFILE

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

pickup = BlueDartPickupRequest(PROFILE)

# Shipper Details
pickup.request.AreaCode = "BOM"
pickup.request.ContactPersonName = "Vatsal Shah"
pickup.request.CustomerAddress1 = "Craftsvilla"
pickup.request.CustomerAddress2 = "G-1502 Lotus Business Park"
pickup.request.CustomerAddress3 = "Goregoan East"
pickup.request.CustomerCode = "099960"
pickup.request.CustomerName = "Craftsvilla"
pickup.request.CustomerPincode = "400060"
pickup.request.CustomerTelephoneNumber = "7738500880"
pickup.request.MobileTelNo = "7738500880"
pickup.request.NumberofPieces = 1
pickup.request.OfficeCloseTime = "18:00"
pickup.request.ProductCode = "A"
pickup.request.ReferenceNo = "59500198122"
pickup.request.WeightofShipment = 1
pickup.request.VolumeWeight = 1
pickup.request.ShipmentPickupTime = "16:00"
pickup.request.ShipmentPickupDate = "2016-04-19"
pickup.request.SubProducts.string.append("E-Tailing")
pickup.request.isToPayShipper = False


# Fires off the request, sets the 'response' attribute on the object.
pickup.send_request()

print(pickup.response)
