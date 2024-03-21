import argparse
from utils.geofence import GeoFence
from utils.handler import MessageHandler
from communication.transceiver import Transceiver
import asyncio

if __name__ == '__main__':



    parser = argparse.ArgumentParser()
    parser.add_argument('--config_communication', type=str, default='../config/communicationConfig.json', help='Path to the communication configuration file')
    parser.add_argument('--config_geofences', type=str, default='../config/GeoFences.json', help='Path to the geofences configuration file')
    args = parser.parse_args()
    geofence = GeoFence()
    geofence.add_geofences(args.config_geofences)
    print("Geofences configuration read and initialized")
    transceiver = Transceiver()
    transceiver.add_messengers(args.config_communication)
    print("Transceiver configuration read and initialized")
    receiver_bsm_index = transceiver.identify_bsm_receiver()
    receiver_psm_index = transceiver.identify_psm_receiver()
    sender_tim_index = transceiver.identify_tim_sender()
    sender_psm_index = transceiver.identify_psm_sender()
    print("Identified receivers and senders")
    handler = MessageHandler()
    handler.update_geofencer(geofence)
    asyncio.run(handler.main(transceiver.receivers[receiver_bsm_index], 
                              transceiver.receivers[receiver_psm_index],
                              transceiver.senders[sender_tim_index],
                              transceiver.senders[sender_psm_index]))
    print("Handler started working")            