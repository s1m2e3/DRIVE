from .sender import Sender
from .receiver import Receiver
import asyncio
import json

class Transceiver:
    def __init__(self):
        """
        Constructor for the class. Initializes the receivers and senders lists.
        """
        self.receivers:list[Receiver] = []
        self.senders:list[Sender] = []
    def add_messengers(self, filename:str):
        """
        Add receivers and senders based on the provided filename.

        Parameters:
            filename (str): The name of the file to open and read communication data from.

        Returns:
            None
        """
        with open(filename, 'r') as f:
            communication_json = json.load(f)

        for receiver in communication_json['receivers']:
            self.receivers.append(Receiver(message_type = receiver['messageType'], ip = receiver['ip'], port = receiver['port']))

        for sender in communication_json['senders']:
            self.senders.append(Sender(message_type = sender['messageType'],host_ip = sender['host_ip'],host_port = sender['host_port'],
            receiver_ip = sender['receiver_ip'], receiver_port = sender['receiver_port']))
    def identify_bsm_receiver(self):
        """
        Returns a list of indices corresponding to the receivers in the `receivers` list that have a message type of "BSM".

        Parameters:
            self (object): The instance of the class.

        Returns:
            list: A list of indices corresponding to the receivers with a message type of "BSM".
        """
        return [self.receivers.index(receiver) for receiver in self.receivers if receiver.message_type == "BSM"]
    def identify_psm_receiver(self):
        """
        Returns a list of indices corresponding to the receivers in the `receivers` list that have a message type of "PSM".

        Parameters:
            self (object): The instance of the class.

        Returns:
            list: A list of indices corresponding to the receivers with a message type of "PSM".
        """
        return [self.receivers.index(receiver) for receiver in self.receivers if receiver.message_type == "PSM"]

    def identify_tim_sender(self):
        """
        Returns a list of indices corresponding to the senders in the `senders` list that have a message type of "TIM".

        Parameters:
            self (object): The instance of the class.

        Returns:
            list: A list of indices corresponding to the senders with a message type of "TIM".
        """
        return [self.senders.index(sender) for sender in self.senders if sender.message_type == "TIM"]
    def identify_psm_sender(self):
        """
        Returns a list of indices corresponding to the senders in the `senders` list that have a message type of "PSM".

        Parameters:
            self (object): The instance of the class.

        Returns:
            list: A list of indices corresponding to the senders with a message type of "PSM".
        """
        return [self.senders.index(sender) for sender in self.senders if sender.message_type == "PSM"]
    async def start_bsm_receiver(self):
        """
        Starts all BSM receivers in the `receivers` list.

        Parameters:
            self (object): The instance of the class.

        Returns:
            None
        """
        indexes = self.identify_bsm_receiver()
        tasks = []
        for index in indexes:
            self.receivers[index].start_receiving()
            tasks.append(self.receivers[index].receive())
        await asyncio.gather(*tasks)
        
        