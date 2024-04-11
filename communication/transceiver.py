from .sender import Sender
from .receiver import Receiver
from enum import Enum
import asyncio
import json

class TransceiverType(Enum):
    BSM = 0
    TIM = 1
    PSM = 2

class Transceiver:
    def __init__(self,kind:TransceiverType):
        self.kind = kind
        self.receiver = None
        self.sender = None
        self.stored_messages = []
        
    def add_messengers(self, filename:str):
        """
        Add receivers and senders based on the provided filename given type.

        Parameters:
            filename (str): The name of the file to open and read communication data from.

        Returns:
            None
        """
        with open(filename, 'r') as f:
            communication_json = json.load(f)

        if self.kind == TransceiverType.BSM:
            receivers = [conf['messageType'] for conf in communication_json['receivers']]
            receiver_bsm_index = receivers.index('BSM')
            bsm_conf = communication_json['receivers'][receiver_bsm_index]
            self.receiver = Receiver(message_type = bsm_conf['messageType'],ip = bsm_conf['ip'], port = bsm_conf['port'])

        elif self.kind == TransceiverType.TIM:
            senders = [conf['messageType'] for conf in communication_json['senders']]
            sender_tim_index = senders.index('TIM')
            tim_conf = communication_json['senders'][sender_tim_index]
            self.sender = Sender(message_type = tim_conf['messageType'],host_ip = tim_conf['host_ip'],host_port = tim_conf['host_port'],
                                 receiver_ip=tim_conf['receiver_ip'], receiver_port = tim_conf['receiver_port'])
        
        elif self.kind == TransceiverType.PSM:
            receivers = [conf['messageType'] for conf in communication_json['receivers']]
            receiver_psm_index = receivers.index('PSM')
            psm_conf = communication_json['receivers'][receiver_psm_index]
            self.receiver = Receiver(message_type = psm_conf['messageType'],ip = psm_conf['ip'], port = psm_conf['port'])

            senders = [conf['messageType'] for conf in communication_json['senders']]
            sender_psm_index = senders.index('PSM')
            psm_conf = communication_json['senders'][sender_psm_index]
            self.sender = Sender(message_type = psm_conf['messageType'],host_ip = psm_conf['host_ip'],host_port = psm_conf['host_port'],
                                 receiver_ip=psm_conf['receiver_ip'], receiver_port = psm_conf['receiver_port'])

    async def store_message(self):
        """
        Asynchronously stores messages received by the receiver in the `stored_messages` list.

        This function continuously appends the received message to the `stored_messages` list
        until the receiver is `None`. It uses an infinite loop and the `asyncio.sleep` function
        to periodically check for new messages.

        Parameters:
            None

        Returns:
            None
        """
        
        if self.receiver is not None:
            while True:
                self.stored_messages.append(self.receiver.message)
                await asyncio.sleep(0.01)

    async def update_message_from_list(self):
    	
        """
    	Asynchronously updates the message that the sender will send from the stored messages list.
    	
    	This function checks if the `sender` attribute is not `None` and if the `stored_messages` list is not empty. If both conditions are met, it enters a while loop. Inside the loop, it calls the `update_message` method of the `sender` object with the last element of the `stored_messages` list. It then waits for 0.1 seconds using `asyncio.sleep` before continuing the loop.
    	
    	This function does not take any parameters and does not return any values.
    	"""

        if self.sender is not None and len(self.stored_messages)>0:
            while True:
                self.sender.update_message(self.stored_messages[-1]) 
                await asyncio.sleep(0.01)

    async def start(self):
        """
        Starts receiver and/or sender given type of Transceiver.

        Parameters:
            self (object): The instance of the class.

        Returns:
            None
        """
        if self.kind == TransceiverType.BSM:
            self.receiver.start_receiving()
            t1= asyncio.create_task(self.store_message())
            t2 = asyncio.create_task(self.receiver.receive()) 
            await asyncio.gather(t1,t2)
            
        elif self.kind == TransceiverType.TIM:
            self.sender.start_sending()
            await self.sender.send()
        elif self.kind == TransceiverType.PSM:
            self.receiver.start_receiving()
            self.sender.start_sending()
            
            t1=asyncio.create_task(self.store_message())
            t2=asyncio.create_task(self.update_message_from_list())
            t3=asyncio.create_task(self.receiver.receive())
            t4=asyncio.create_task(self.sender.send())
            await asyncio.gather(t1,t2,t3,t4)
        
        
        