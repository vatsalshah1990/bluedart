from datetime import datetime
import logging

import sys

# Un-comment to see the response from Bluedart printed in stdout.
from bluedart.services.ship_service import BlueDartProcessShipmentRequest
from examples.example_profile import PROFILE

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

shipment = BlueDartProcessShipmentRequest(PROFILE)

# Sender Details
shipment.Request.Shipper.CustomerAddress1 = "Craftsvilla"
shipment.Request.Shipper.CustomerAddress2 = "G-1502 Lotus Business Park"
shipment.Request.Shipper.CustomerAddress3 = "Goregoan East"
shipment.Request.Shipper.CustomerCode = "099960"
shipment.Request.Shipper.CustomerMobile = "7738500880"
shipment.Request.Shipper.CustomerTelephone = "7738500880"
shipment.Request.Shipper.CustomerName = "Ankit Kante"
shipment.Request.Shipper.CustomerPincode = "400060"
shipment.Request.Shipper.OriginArea = "BOM"
shipment.Request.Shipper.Sender = "The Avengers"

# Consignee Details
shipment.Request.Consignee.ConsigneeAddress1 = "Flat no. C-601"
shipment.Request.Consignee.ConsigneeAddress2 = "Eden II CHS Ltd"
shipment.Request.Consignee.ConsigneeAddress3 = "Hiranandani Gardens, Powai"
shipment.Request.Consignee.ConsigneeMobile = "7738500880"
shipment.Request.Consignee.ConsigneeName = "Vatsal Shah"
shipment.Request.Consignee.ConsigneePincode = "400076"
shipment.Request.Consignee.ConsigneeTelephone = "7738500880"

# Items Details
shipment.Request.Services.ActualWeight = 0.5
shipment.Request.Services.CollectableAmount = 100
shipment.Request.Services.Commodity.CommodityDetail1 = "Shoes"
shipment.Request.Services.Commodity.CommodityDetail2 = "Black"
shipment.Request.Services.Commodity.CommodityDetail3 = "Nike"
shipment.Request.Services.CreditReferenceNo = "1232132349"
shipment.Request.Services.DeclaredValue = 100
dimension = shipment.client.factory.create("ns2:Dimension")
dimension.Breadth = 10
dimension.Height = 10
dimension.Length = 10
dimension.Count = 1
shipment.Request.Services.Dimensions.Dimension.append(dimension)
shipment.Request.Services.InvoiceNo = "97283489"
shipment.Request.Services.PickupDate = datetime.now().date()
shipment.Request.Services.PickupTime = "1800"
shipment.Request.Services.PieceCount = 1
shipment.Request.Services.ProductCode = "A"
shipment.Request.Services.ProductType = "Dutiables"
shipment.Request.Services.SubProductCode = "C"

# Fires off the request, sets the 'response' attribute on the object.
shipment.send_request()

print(shipment.response)

