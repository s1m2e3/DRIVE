from message import Message, MessageType
from typing import List
from data_classes import Extent, FullPositionVector 
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
        self.kind = MessageType.RSA
    def add_road_side_alert(self, road_side_alert):
        
        road_side_alert = asdict(road_side_alert)
        print(road_side_alert)
        if road_side_alert['extent'] is not None:
            road_side_alert['extent'] = road_side_alert['extent'].value
        if road_side_alert['position'] is not None:
            if road_side_alert['position']['timeConfidence'] is not None:
                road_side_alert['position']['timeConfidence'] = road_side_alert['position']['timeConfidence'].value
            if road_side_alert['position']['posConfidence']['pos'] is not None:
                road_side_alert['position']['posConfidence']['pos'] = road_side_alert['position']['posConfidence']['pos'].value
            if road_side_alert['position']['posConfidence']['elevation'] is not None:
                road_side_alert['position']['posConfidence']['elevation'] = road_side_alert['position']['posConfidence']['elevation'].value
            if road_side_alert['position']['speedConfidence']['speed'] is not None:
                road_side_alert['position']['speedConfidence']['speed'] = road_side_alert['position']['speedConfidence']['speed'].value
            if road_side_alert['position']['speedConfidence']['heading'] is not None:
                road_side_alert['position']['speedConfidence']['heading'] = road_side_alert['position']['speedConfidence']['heading'].value
            if road_side_alert['position']['speedConfidence']['throttle'] is not None:
                road_side_alert['position']['speedConfidence']['throttle'] = road_side_alert['position']['speedConfidence']['throttle'].value
        
        self.data.update(road_side_alert)
