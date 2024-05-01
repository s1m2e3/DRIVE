from .sender import Sender
from .receiver import Receiver
from enum import Enum
import asyncio
import json
from typing import Union
from ..messages.message import Message, MessageType
class TransceiverType(Enum):
    BSM = 0
    TIM = 1
    PSM = 2
    RSA = 3

class Transceiver:
    def __init__(self):
        self.receivers = {}
        self.senders = {}
        self.stored_messages = {}
        
    def add_messengers_from_conf(self, filename:str):
        """
        Add receivers and senders based on the provided filename given type.

        Parameters:
            filename (str): The name of the file to open and read communication data from.

        Returns:
            None
        """
        with open(filename, 'r') as f:
            communication_json = json.load(f)
        senders_geofence_id = [conf['geofence_id'] for conf in communication_json['senders']]
        receivers_geofence_id = [conf['geofence_id'] for conf in communication_json['receivers']]
        
        message_types_by_sender = {conf['geofence_id']:[] for conf in communication_json['senders']}
        message_types_by_receiver = {conf['geofence_id']:[] for conf in communication_json['receivers']}
        
        for conf in communication_json['senders']:
            message_types_by_sender[conf['geofence_id']].append(conf['messageType'])

        for conf in communication_json['receivers']:
            message_types_by_receiver[conf['geofence_id']].append(conf['messageType'])

        for geofence_id in senders_geofence_id:
            if geofence_id not in self.senders:
                self.senders[geofence_id] = {}
            for message_type in message_types_by_sender[geofence_id]:
                if message_type not in self.senders[geofence_id]:
                    receiving_port = communication_json['senders'][senders_geofence_id.index(geofence_id)]['receiving_port']
                    receiving_ip = communication_json['senders'][senders_geofence_id.index(geofence_id)]['receiving_ip']
                    host_port = communication_json['senders'][senders_geofence_id.index(geofence_id)]['host_port']
                    host_ip = communication_json['senders'][senders_geofence_id.index(geofence_id)]['host_ip']
                    self.senders[geofence_id][message_type] = Sender(host_ip=host_ip, host_port=host_port, receiver_ip=receiving_ip, receiver_port=receiving_port, message_type=message_type, message="")
                    
        for geofence_id in receivers_geofence_id:
            if geofence_id not in self.receivers:
                self.receivers[geofence_id] = {}
            if geofence_id not in self.stored_messages:
                self.stored_messages[geofence_id] = []
            for message_type in message_types_by_receiver[geofence_id]:
                if message_type not in self.receivers[geofence_id]:
                    port = communication_json['receivers'][receivers_geofence_id.index(geofence_id)]['port']
                    ip = communication_json['receivers'][receivers_geofence_id.index(geofence_id)]['ip']
                    self.receivers[geofence_id][message_type] = Receiver(ip=ip, port=port)
                if message_type not in self.stored_messages[geofence_id]:
                    self.stored_messages[geofence_id][message_type] = []

    async def store_messages(self):
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
        
        if self.receivers is not None:
            while True:
                for geofence_id in self.receivers:
                    for message_type in self.receivers[geofence_id]:
                        self.stored_messages[geofence_id][message_type].append(self.receivers[geofence_id][message_type].message)
                await asyncio.sleep(0.01)

    async def update_message_from_list(self):
    	
        """
    	Asynchronously updates the message that the sender will send from the stored messages list.
    	
    	This function checks if the `sender` attribute is not `None` and if the `stored_messages` list is not empty. If both conditions are met, it enters a while loop. Inside the loop, it calls the `update_message` method of the `sender` object with the last element of the `stored_messages` list. It then waits for 0.1 seconds using `asyncio.sleep` before continuing the loop.
    	
    	This function does not take any parameters and does not return any values.
    	"""

        if self.senders is not None and len(self.stored_messages)>0:
            while True:
                for geofence_id in self.receivers:
                    for message_type in self.receivers[geofence_id]:
                        self.senders[geofence_id][message_type].update_message(self.stored_messages[geofence_id][message_type].pop(0))
                await asyncio.sleep(0.01)

    async def add_mobile(self, geofence_id):
        """
        Asynchronously adds a sender to the `senders` attribute.

        Parameters:
            sender (Sender): The sender to be added.

        Returns:
            None
        """
        geofence_id = sender.geofence_id
        message_type = sender.message_type
    
    async def start(self):
        
        """
        Asynchronously starts sending and receiving messages also updates the message that the sender will send and stores the received messages.

        Parameters:
            self (object): The instance of the class.

        Returns:
            None
        """

        
        tasks = []
        
        if self.senders is not None:
            for geofence_id in self.senders:
                for message_type in self.senders[geofence_id]:
                    t = asyncio.create_task(self.senders[geofence_id][message_type].send())
                    tasks.append(t)
        
        if self.receivers is not None:
            for geofence_id in self.receivers:
                for message_type in self.receivers[geofence_id]:
                    t = asyncio.create_task(self.receivers[geofence_id][message_type].receive())
                    tasks.append(t)
        
        t = asyncio.create_task(self.store_messages())
        tasks.append(t)
        
        t = asyncio.create_task(self.update_message_from_list())
        tasks.append(t)
        
        await asyncio.gather(*tasks)



       
        
        