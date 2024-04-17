import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from communication.transceiver import Transceiver, TransceiverType
from messages.PSM import PSM,PersonalSafetyMessage
from messages.data_classes import TravelerInfoType,Position3D,PositionalAccuracy
import asyncio

sender = Transceiver(TransceiverType.PSM)
sender.add_messengers('../../config/communicationConfig.json')
psm_message = PSM()
personal_safety_message = PersonalSafetyMessage(basicType=TravelerInfoType.roadSignage.value,
    secMark=0, msgCnt=0, id='\x00\x00\x00\x00\x00\x00\x00\x00',
    position=Position3D(lat=0, lon=0), accuracy=PositionalAccuracy(semiMajor=0, semiMinor=0, orientation=0), speed=0, heading=0)

psm_message.add_personal_safety_message(personal_safety_message)
sender.sender.update_message(psm_message.to_json())
sender.sender.start_sending()
try:
    asyncio.run(sender.sender.send())
except KeyboardInterrupt:
    print("Gracefully closing... PSM transceiver script")

