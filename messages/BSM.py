
from message import Message, MessageType
from typing import List
from data_classes import BSMcoreData
from typing import Optional
from dataclasses import dataclass, asdict

@dataclass
class BasicSafetyMessage():
    coreData : BSMcoreData

class BSM(Message):
    def __init__(self):
        super().__init__()
        self.kind = MessageType.BSM
    def add_personal_safety_message(self, personal_safety_message):
        personal_safety_message = asdict(personal_safety_message)
        personal_safety_message['basicType'] = personal_safety_message['basicType'].value
        self.data.update(personal_safety_message)