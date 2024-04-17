from data_classes import *
from message import Message, MessageType
from TIM import DataFrame, TIM
from PSM import PSM, PersonalSafetyMessage
from RSA import RSA, RoadSideAlert
from typing import Union
class Inspector():
    def __init__(self, message_type:Union[MessageType.BSM,MessageType.TIM,MessageType.PSM,MessageType.RSA]):
        self.message_type = message_type
    def inspect_receiving(self):
        kind = self.message
    def inspect_sending(self,message):
        
        if self.message_type == MessageType.BSM:
            message_object = BSM()
        elif self.message_type == MessageType.TIM:
            pass
        elif self.message_type == MessageType.PSM:
            pass
        elif self.message_type == MessageType.RSA:
            pass
        return message_object,message