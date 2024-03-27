from message import Message
from dataclasses import dataclass, asdict
from data_classes import TravelerInfoType, RoadSignID, GeographicalPath, Advisory, WorkZone, GenericSign, SpeedLimit, ExitService
from typing import Union,List
@dataclass
class DataFrame:
    frameType: TravelerInfoType
    msgID: Union[bytes, RoadSignID]
    startTime : int
    durationTime : int
    priority: int
    regions: List[GeographicalPath]
    content: Union[Advisory,WorkZone,GenericSign,SpeedLimit,ExitService]

class TIM(Message):
    def __init__(self):
        super().__init__()
        self.data["dataFrames"]= []
    def add_data_frame(self, data_frame):
        data_frame = asdict(data_frame)
        self.data["dataFrames"].append(data_frame)



