from ..communication.receiver import Receiver
from ..communication.sender import Sender
import time 
import asyncio
class MessageHandler():
    def __init__(self,timeout_message_bsm:int = 600,timeout_message_tim:int = 600,timeout_message_psm:int = 600):
        self.active_bsm = []
        self.active_tim = []
        self.active_psm = []
        self.timeout_message_bsm = timeout_message_bsm
        self.timeout_message_tim = timeout_message_tim
        self.timeout_message_psm = timeout_message_psm

    async def update_bsm_list(self,receiver:Receiver):
        async for message in receiver.update_message():
            self.active_bsm.append(message)
    async def update_psm_list(self,receiver:Receiver):
        async for message in receiver.update_message():
            self.active_psm.append(message)
    async def update_tim(self,sender:Sender):
        while True:
            message = self.active_tim[-1]
            sender.update_message(message)
            await asyncio.sleep(0.1)
    async def update_psm(self,sender:Sender):
        while True:
            message = self.active_psm[-1]
            sender.update_message(message)
            await asyncio.sleep(0.1)  
    async def remove_bsm(self):
        while True:
            for bsm in self.active_bsm:
                if bsm['timestamp'] + self.timeout_message_bsm < time.time():
                    self.active_bsm.remove(bsm)
            await asyncio.sleep(60)
    async def remove_tim(self):
        while True:
            for tim in self.active_tim:
                if tim['timestamp'] + self.timeout_message_tim < time.time():
                    self.active_tim.remove(tim)
            await asyncio.sleep(60)
    async def remove_psm(self):
        while True:
            for psm in self.active_psm:
                if psm['timestamp'] + self.timeout_message_psm < time.time():
                    self.active_psm.remove(psm)
            await asyncio.sleep(60)

    