import json
import time
from enum import Enum
class MessageType(Enum):
    BSM = 0
    TIM = 1
    PSM = 2
    RSA = 3
    REGISTRATION = 4

class Message():
    def __init__(self):
        self.kind = None
        self.data:dict = {}
        self.update_timestamp()
    def from_json(self, json_str):
        self.data = json.loads(json_str)
    def to_json(self):
        return json.dumps(self.data)
    def from_json(self, json_str):
        self.data = json.loads(json_str)
    def update_timestamp(self):
        self.data["timeStamp"] = self.get_timestamp()
    def get_timestamp(self):
        return int(round(time.time() * 1000))
    
