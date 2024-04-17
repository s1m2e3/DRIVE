from message import Message, MessageType
from dataclasses import dataclass, asdict
from data_classes import PersonalDeviceUserType, Position3D, PositionalAccuracy
from typing import Union,List, Optional
@dataclass
class PersonalSafetyMessage:
    basicType : PersonalDeviceUserType 
    secMark : int
    msgCnt : int 
    id : bytes 
    position : Position3D 
    accuracy : PositionalAccuracy 
    speed : int 
    heading : int


class PSM(Message):
    def __init__(self):
        super().__init__()
        self.kind = MessageType.PSM
    def add_personal_safety_message(self, personal_safety_message):
        personal_safety_message = asdict(personal_safety_message)
        self.data.update(personal_safety_message)