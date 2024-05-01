from geofence import GeoFence
from ..communication.receiver import Receiver
from ..messages.message import MessageType
import json
import asyncio

class Client():
    def __init__(self):
        self.mobiles_registered = []
        self.transceiver = None
        self.geofencer = GeoFence()
    
    def add_registration_receiver(self, filename:str):
        """
        Add registration receivers based on the provided filename given type.

        Parameters:
            filename (str): The name of the file to open and read communication data from.

        Returns:
            None
        """
        with open(filename, 'r') as f:
            communication_json = json.load(f)

        receivers = [conf['messageType'] for conf in communication_json['receivers']]
        receiver_registration_index = receivers.index('REGISTRATION')
        registration_conf = communication_json['receivers'][receiver_registration_index]
        self.receiver = Receiver(message_type = MessageType.REGISTRATION,ip = registration_conf['ip'], port = registration_conf['port'])

    async def add_receiver_from_message(self):
        """
        Asynchronously adds a receiver based on the message received. Checks if the message is not None, performs geofencing to determine if the message is within a geofence,
        adds the mobile ID to the registered list if it meets the criteria, and yields the geofence ID. 
        """
        while True:
            if self.receiver.message is not None:
                message = self.receiver.message
                within,geofence_id = self.geofencer.in_geofence(message.lat, message.long)
                mobile_id = message.id
                geofence_id_mobile_id = (geofence_id, mobile_id)
                if within and geofence_id_mobile_id not in self.mobiles_registered:
                    self.mobiles_registered.append(geofence_id_mobile_id)
                    await asyncio.sleep(0.1)
                    yield geofence_id
                
