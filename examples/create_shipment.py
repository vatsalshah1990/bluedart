from datetime import datetime
import logging

import sys

# Un-comment to see the response from Fedex printed in stdout.
from bluedart.services.ship_service import BlueDartProcessShipmentRequest
from examples.example_profile import PROFILE

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

shipment = BlueDartProcessShipmentRequest(PROFILE)

# Sender Details
shipment.GenerateWayBill.Request.Shipper.CustomerAddress1 = "Craftsvilla"
shipment.GenerateWayBill.Request.Shipper.CustomerAddress2 = "G-1502 Lotus Business Park"
shipment.GenerateWayBill.Request.Shipper.CustomerAddress3 = "Goregoan East"
shipment.GenerateWayBill.Request.Shipper.CustomerCode = "099960"
shipment.GenerateWayBill.Request.Shipper.CustomerMobile = "7738500880"
shipment.GenerateWayBill.Request.Shipper.CustomerTelephone = "7738500880"
shipment.GenerateWayBill.Request.Shipper.CustomerName = "Ankit Kante"
shipment.GenerateWayBill.Request.Shipper.CustomerPincode = "400060"
shipment.GenerateWayBill.Request.Shipper.OriginArea = "BOM"
shipment.GenerateWayBill.Request.Shipper.Sender = "The Avengers"

# Consignee Details
shipment.GenerateWayBill.Request.Consignee.ConsigneeAddress1 = "Flat no. C-601"
shipment.GenerateWayBill.Request.Consignee.ConsigneeAddress2 = "Eden II CHS Ltd"
shipment.GenerateWayBill.Request.Consignee.ConsigneeAddress3 = "Hiranandani Gardens, Powai"
shipment.GenerateWayBill.Request.Consignee.ConsigneeMobile = "7738500880"
shipment.GenerateWayBill.Request.Consignee.ConsigneeName = "Vatsal Shah"
shipment.GenerateWayBill.Request.Consignee.ConsigneePincode = "400076"
shipment.GenerateWayBill.Request.Consignee.ConsigneeTelephone = "7738500880"

# Items Details
shipment.GenerateWayBill.Request.Services.ActualWeight = 0.5
shipment.GenerateWayBill.Request.Services.CollectableAmount = 100
shipment.GenerateWayBill.Request.Services.Commodity.CommodityDetail1 = "Shoes"
shipment.GenerateWayBill.Request.Services.Commodity.CommodityDetail2 = "Black"
shipment.GenerateWayBill.Request.Services.Commodity.CommodityDetail3 = "Nike"
shipment.GenerateWayBill.Request.Services.CreditReferenceNo = "123123123"
shipment.GenerateWayBill.Request.Services.DeclaredValue = 100
dimension = shipment.client.factory.create("Dimension")
dimension.Breadth = 10
dimension.Height = 10
dimension.Length = 10
dimension.Count = 1
shipment.GenerateWayBill.Request.Services.Dimensions.append(dimension)
shipment.GenerateWayBill.Request.Services.InvoiceNo = "97283489"
shipment.GenerateWayBill.Request.Services.PickupDate = datetime.now().date()
shipment.GenerateWayBill.Request.Services.PickupTime = "1800"
shipment.GenerateWayBill.Request.Services.PieceCount = 1
shipment.GenerateWayBill.Request.Services.ProductCode = "A"
shipment.GenerateWayBill.Request.Services.ProductType = "Dutiables"
shipment.GenerateWayBill.Request.Services.SubProductCode = "C"

# Fires off the request, sets the 'response' attribute on the object.
shipment.send_request()

print(shipment.response)

