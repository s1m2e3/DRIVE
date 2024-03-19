import argparse
from utils.geofence import GeoFence
from utils.handler import MessageHandler
from communication.transceiver import Transceiver

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
    handler = MessageHandler()
    