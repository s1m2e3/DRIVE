from .message import Message
from typing import List
from .data_classes import PriorityRequestType,Extent, FullPositionVector 
from typing import Optional
from dataclasses import dataclass, asdict
@dataclass
class RoadSideAlert:
    typeEvent: int
    description: List[int]
    priority: Optional[PriorityRequestType]
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
            self.data.update(road_side_alert)