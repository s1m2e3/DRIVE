import argparse
from utils.geofence import GeoFence
from utils.handler import MessageHandler
from communication.transceiver import Transceiver
import asyncio
from messages.TIM import TIM, DataFrame
from messages.PSM import PSM, PersonalSafetyMessage
from messages.data_classes import TravelerInfoType,Advisory,PersonalDeviceUserType,Position3D,PositionalAccuracy

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
    tim_message = TIM()
    data_frame = DataFrame()
    data_frame.frameType = TravelerInfoType.advisory
    data_frame.msgID = 0
    data_frame.startTime = 0
    data_frame.durationTime = 0
    data_frame.priority = 0
    data_frame.regions = []
    data_frame.content = Advisory()
    tim_message.add_data_frame(data_frame)

    psm_message = PSM()
    personal_safety_message = PersonalSafetyMessage()
    personal_safety_message.basicType = PersonalDeviceUserType.aPEDALCYCLIST
    personal_safety_message.secMark = 0
    personal_safety_message.msgCnt = 0
    personal_safety_message.id = 0
    personal_safety_message.position = Position3D()
    personal_safety_message.accuracy = PositionalAccuracy()
    personal_safety_message.speed = 0
    personal_safety_message.heading = 0

    tim_message.add_data_frame()
    psm_message.add_personal_safety_message()
    tim_message.add_data_frame(psm_message)
    print("Tim and Psm messages added")


    asyncio.run(handler.main(transceiver.receivers[receiver_bsm_index], 
                              transceiver.receivers[receiver_psm_index],
                              transceiver.senders[sender_tim_index],
                              transceiver.senders[sender_psm_index]))
    print("Handler started working")            