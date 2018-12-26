import logging

import sys

# Un-comment to see the response from Bluedart printed in stdout.
from bluedart.services.cancel_pickup_service import BlueDartCancelPickupRequest
from examples.example_profile import PROFILE

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

cancel_pickup = BlueDartCancelPickupRequest(PROFILE)

# Shipper Details
cancel_pickup.request.TokenNumber = '81479'
cancel_pickup.request.PickupRegistrationDate = '2018-12-27T00:00:00'
cancel_pickup.request.Remarks = 'Cancel Pickup Request'

# Fires off the request, sets the 'response' attribute on the object.
cancel_pickup.send_request()

print(cancel_pickup.response)
