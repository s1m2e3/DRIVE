import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from communication.transceiver import Transceiver, TransceiverType
from messages.RSA import RSA, RoadSideAlert
from messages.data_classes import Extent,FullPositionVector
import asyncio

sender = Transceiver(TransceiverType.RSA)
sender.add_messengers('../../config/communicationConfig.json')
rsa_message = RSA()
road_side_alert = RoadSideAlert(typeEvent=1, description=[1234], priority=None, heading=None, extent=None, position=None, furtherInfoID=None, regional=None)
rsa_message.add_road_side_alert(road_side_alert)
sender.sender.update_message(rsa_message.to_json())

try:
    asyncio.run(sender.start())
except KeyboardInterrupt:
    print("Gracefully closing... RSA transceiver script")