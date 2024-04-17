from message import Message, MessageType
from dataclasses import dataclass, asdict
from data_classes import PersonalDeviceUserType, Position3D, PositionalAccuracy
from typing import Union,List, Optional
@dataclass
class PersonalSafetyMessage:
    
    basicType : int = PersonalDeviceUserType.unavailable.value
    secMark : int = 65535
    msgCnt : int = 0
    id : int = 99999999
    position : Position3D = Position3D()
    accuracy : PositionalAccuracy = PositionalAccuracy()
    speed : int  = 8191
    heading : int = 28800

    def __post_init__(self):
        self._validate_inputs()

    def _validate_inputs(self):
        values = [member.value for member in PersonalDeviceUserType]
        if not isinstance(self.basicType, int) or self.basicType < min(values) or self.basicType > max (values):
            raise ValueError("basicType must be an integer between PersonalDeviceUserType.unavailable.value and PersonalDeviceUserType.max_value")
        if not isinstance(self.secMark, int) or self.secMark < 0 or self.secMark > 65535:
            raise ValueError("secMark must be an integer between 0 and 65535")
        if not isinstance(self.msgCnt, int) or self.msgCnt < 0 or self.msgCnt > 65535:
            raise ValueError("msgCnt must be an integer between 0 and 65535")
        if not isinstance(self.id, int) or self.id < 0 or self.id > 99999999:
            raise ValueError("id must be an integer between 0 and 99999999")
        if not isinstance(self.position.lat, float) or self.position.lat < -180.0 or self.position.lat > 180.0:
            raise ValueError("position.lat must be a float between -180.0 and 180.0")
        if not isinstance(self.position.lon, float) or self.position.lon < -180.0 or self.position.lon > 180.0:
            raise ValueError("position.lon must be a float between -180.0 and 180.0")
        if not isinstance(self.accuracy.semiMajor, int) or self.accuracy.semiMajor < 0 or self.accuracy.semiMajor >
    

class PSM(Message):
    def __init__(self):
        super().__init__()
        self.kind = MessageType.PSM
    def add_personal_safety_message(self, personal_safety_message):
        personal_safety_message = asdict(personal_safety_message)
        self.data.update(personal_safety_message)