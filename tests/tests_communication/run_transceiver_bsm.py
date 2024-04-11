import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from communication.transceiver import Transceiver, TransceiverType
from messages.TIM import TIM, DataFrame
from messages.data_classes import TravelerInfoType,RoadSignID,GeographicalPath,Advisory,WorkZone,GenericSign,SpeedLimit,ExitService,Position3D
import asyncio

receiver = Transceiver(TransceiverType.BSM)
receiver.add_messengers('../../config/communicationConfig.json')

try:
    asyncio.run(receiver.start())
except KeyboardInterrupt:
    print("Gracefully closing... BSM transceiver script")