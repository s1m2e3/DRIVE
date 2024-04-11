from message import Message
from typing import List
from data_classes import PriorityRequestType,Extent, FullPositionVector 
from typing import Optional
from dataclasses import dataclass, asdict
@dataclass
class RoadSideAlert:
    typeEvent: int
    description: List[int]
    priority: Optional[bytes]
    heading : Optional[bytes]
    extent : Optional[Extent]
    position : Optional[FullPositionVector]
    furtherInfoID : bytes
    regional : Optional[List[dict]]

class RSA(Message):
    def __init__(self):
        super().__init__()

    def add_road_side_alert(self, road_side_alert):
        
        road_side_alert = asdict(road_side_alert)
        road_side_alert['extent'] = road_side_alert['extent'].value
        road_side_alert['FullPositionVector']['TimeConfidence'] = road_side_alert['FullPositionVector']['TimeConfidence'].value
        road_side_alert['FullPositionVector']['posConfidence']['pos'] = road_side_alert['FullPositionVector']['posConfidence']['pos'].value
        road_side_alert['FullPositionVector']['posConfidence']['elevation'] = road_side_alert['FullPositionVector']['posConfidence']['elevation'].value
        road_side_alert['FullPositionVector']['speedConfidence']['speed'] = road_side_alert['FullPositionVector']['speedConfidence']['speed'].value
        road_side_alert['FullPositionVector']['speedConfidence']['heading'] = road_side_alert['FullPositionVector']['speedConfidence']['heading'].value
        road_side_alert['FullPositionVector']['speedConfidence']['throttle'] = road_side_alert['FullPositionVector']['speedConfidence']['throttle'].value
        self.data.update(road_side_alert)
