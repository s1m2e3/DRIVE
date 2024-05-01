
from message import Message, MessageType
from typing import List
from data_classes import BSMcoreData
from typing import Optional
from dataclasses import dataclass, asdict



class BSM(Message):
    def __init__(self):
        super().__init__()
        self.kind = MessageType.BSM
    def add_basic_safety_message(self, basic_safety_message):
        basic_safety_message = asdict(basic_safety_message)
        basic_safety_message['basicType'] = basic_safety_message['basicType'].value
        self.data.update(personal_safety_message)