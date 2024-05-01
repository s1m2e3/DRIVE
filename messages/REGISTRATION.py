from message import Message, MessageType
from dataclasses import dataclass, asdict
from data_classes import Registration
class REGISTRATION(Message):
    def __init__(self):
        super().__init__()
        self.kind = MessageType.REGISTRATION
    def add_registration(self, registration:Registration):
        registration = asdict(registration)
        self.data.update(registration)