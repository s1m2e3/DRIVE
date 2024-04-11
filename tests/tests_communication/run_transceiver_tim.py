import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from communication.transceiver import Transceiver, TransceiverType
from messages.TIM import TIM, DataFrame
from messages.data_classes import TravelerInfoType,RoadSignID,GeographicalPath,Advisory,WorkZone,GenericSign,SpeedLimit,ExitService,Position3D
import asyncio

sender = Transceiver(TransceiverType.TIM)
sender.add_messengers('../../config/communicationConfig.json')
tim_message = TIM()
data_frame = DataFrame(frameType=TravelerInfoType.roadSignage,
                       msgID='\x68\x65\x6c\x6c\x6f',
                       startTime=0, durationTime=0, priority=0,
                       regions=[GeographicalPath(name=None, id=None, anchor=Position3D(lat=0, lon=0), laneWidth=None, closedPath=None, direction=None)],
                       content=Advisory(item=1234))
tim_message.add_data_frame(data_frame)
sender.sender.update_message(tim_message.to_json())
try:
    asyncio.run(sender.start())
except KeyboardInterrupt:
    print("Gracefully closing... TIM transceiver script")