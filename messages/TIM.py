from message import Message,MessageType
from dataclasses import dataclass, asdict
from data_classes import TravelerInfoType, RoadSignID, GeographicalPath, Advisory, WorkZone, GenericSign, SpeedLimit, ExitService
from typing import Union,List


class TIM(Message):
    def __init__(self):
        super().__init__()
        self.kind = MessageType.TIM
        self.data["dataFrames"]= []
    def add_data_frame(self, data_frame):
        data_frame = asdict(data_frame)
        data_frame['frameType'] = data_frame['frameType'].value
        self.data["dataFrames"].append(data_frame)
    


