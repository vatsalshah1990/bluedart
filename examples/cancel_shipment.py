import logging

import sys

# Un-comment to see the response from Bluedart printed in stdout.
from bluedart.services.ship_service import BlueDartCancelShipmentRequest
from examples.example_profile import PROFILE

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

shipment = BlueDartCancelShipmentRequest(PROFILE)

shipment.Request.AWBNo = "59500198122"

# Fires off the request, sets the 'response' attribute on the object.
shipment.send_request()

print(shipment.response)
