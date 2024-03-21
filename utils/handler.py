from ..communication.receiver import Receiver
from ..communication.sender import Sender
from .geofence import GeoFence
import time 
import asyncio
import typing
class MessageHandler():
    def __init__(self,timeout_message_bsm:int = 600,timeout_message_tim:int = 600,timeout_message_psm:int = 600):
        """
        Initializes the class with timeout values for different types of messages.

        Args:
            timeout_message_bsm (int): Timeout value for BSM messages.
            timeout_message_tim (int): Timeout value for TIM messages.
            timeout_message_psm (int): Timeout value for PSM messages.
        """
        self.active_bsm = []
        self.active_tim = []
        self.active_psm = []
        self.timeout_message_bsm = timeout_message_bsm
        self.timeout_message_tim = timeout_message_tim
        self.timeout_message_psm = timeout_message_psm
        self.geofencer = None
    async def update_bsm_list(self,receiver_list: list[Receiver]):
        """
        Asynchronously updates the list of active BSMs by iterating over the messages received from each receiver in `receiver_list`.
        The points are only appended if they are inside the geofence.

        Args:
            receiver_list (List[Receiver]): A list of receiver objects from which to retrieve messages.

        Returns:
            None
        """
        for receiver in receiver_list:
            async for message in receiver.update_message():
                lat = message['coreData']['lat']
                long = message['coreData']['long']
                within,_ =  self.geofence.in_geofence(lat,long)
                if within:
                    self.active_bsm.append(message)

    async def update_psm_list(self,receiver_list: list[Receiver]):
        """
        Asynchronously updates the list of active PSMs by iterating over the messages received from each receiver in `receiver_list`.

        Args:
            receiver_list (List[Receiver]): A list of receiver objects from which to retrieve messages.

        Returns:
            None
        """
        for receiver in receiver_list:
            async for message in receiver.update_message():
                self.active_psm.append(message)
            
    async def update_tim(self,sender_list: list[Sender]):
        """
        Asynchronously updates the last message in the active_tim list with the given sender.

        Args:
            sender_list (List[Sender]): The list of sender objects to update the message with.

        Returns:
            None
        """
        
        while True:
            for sender in sender_list:
                message = self.active_tim[-1]
                sender.update_message(message)
            await asyncio.sleep(0.1)

    async def update_psm(self,sender_list: list[Sender]):
        """
        Asynchronously updates the last message in the active_psm list with the given sender objects.

        Args:
            sender_list (List[Sender]): The list of sender objects to update the messages with.

        Returns:
            None
        """
        while True:
            for sender in sender_list:
                message = self.active_psm[-1]
                sender.update_message(message)
            await asyncio.sleep(0.1)  
            
    async def remove_bsm(self):
        """
        Asynchronously removes expired BSM messages from the active_bsm list.

        This function continuously checks the active_bsm list for expired BSM messages and removes them. The expiration time is determined by the timestamp of each BSM message plus the timeout_message_bsm value.

        Parameters:
            self (object): The instance of the class.

        Returns:
            None

        Raises:
            None
        """
        while True:
            for bsm in self.active_bsm:
                if bsm['timestamp'] + self.timeout_message_bsm < time.time():
                    self.active_bsm.remove(bsm)
            await asyncio.sleep(60)
            
    async def remove_tim(self):
        """
        Asynchronously removes timed out messages from the active_tim list.

        This function continuously checks the active_tim list for any messages that have exceeded the timeout period. If a message's timestamp plus the timeout_message_tim value is less than the current time, the message is removed from the active_tim list.

        Parameters:
            None

        Returns:
            None
        """
        while True:
            for tim in self.active_tim:
                if tim['timestamp'] + self.timeout_message_tim < time.time():
                    self.active_tim.remove(tim)
            await asyncio.sleep(60)
            
    async def remove_psm(self):
        """
        Asynchronously removes expired PSMs from the active_psm list.

        This function continuously checks the active_psm list for PSMs that have exceeded the timeout period. If a PSM's timestamp plus the timeout_message_psm value is less than the current time, it is removed from the list. The function runs indefinitely, with a delay of 60 seconds between each iteration.

        Parameters:
            None

        Returns:
            None
        """
        while True:
            for psm in self.active_psm:
                if psm['timestamp'] + self.timeout_message_psm < time.time():
                    self.active_psm.remove(psm)
            await asyncio.sleep(60)

    async def main(self, receiver_bsm_list: list[Receiver], receiver_psm_list: list[Receiver],
                    sender_tim_list: list[Sender], sender_psm_list: list[Sender]):
        """
        Asynchronously collects all the list updating and removing tasks and runs them concurrently.
        
        :param receiver_bsm: Receiver object for BSM
        :param receiver_psm: Receiver object for PSM
        :param sender_tim: Sender object for TIM
        :param sender_psm: Sender object for PSM
        :return: None
        """
        if self.geofence is None:
            raise Exception("Geofence not initialized, the main function can't start without a geofence object")
        else:
            tasks = [
                self.update_bsm_list(receiver_bsm_list),
                self.update_psm_list(receiver_psm_list),
                self.update_tim(sender_tim_list),
                self.update_psm(sender_psm_list),
                self.remove_bsm(),
                self.remove_tim(),
                self.remove_psm()
            ]
            await asyncio.gather(*tasks)
    
    def update_geofencer(self,geofence: GeoFence):
        """
        Updates the geofence object with the given GeoFence object.

        Args:
            geofence (GeoFence): The GeoFence object to update the geofence with.

        Returns:
            None
        """
        self.geofence = geofence