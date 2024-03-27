import json
import time
class Message():
    def __init__(self):
        self.data:dict = {}
        self.update_timestamp()
    def to_json(self):
        return json.dumps(self.data)
    def from_json(self, json_str):
        self.data = json.loads(json_str)
    def update_timestamp(self):
        self.data["timestamp"] = self.get_timestamp()
    def get_timestamp(self):
        return int(round(time.time() * 1000))

