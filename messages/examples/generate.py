from ..PSM import PSM,PersonalSafetyMessage
from ..TIM import TIM, DataFrame
from ..RSA import RSA, RoadSideAlert
from ..data_classes import TravelerInfoType,Position3D,PositionalAccuracy,GeographicalPath,Advisory
import json

psm_message = PSM()
personal_safety_message = PersonalSafetyMessage(basicType=TravelerInfoType.roadSignage,
    secMark=0, msgCnt=0, id='\x00\x00\x00\x00\x00\x00\x00\x00',
    position=Position3D(lat=0, lon=0), accuracy=PositionalAccuracy(semiMajor=0, semiMinor=0, orientation=0), speed=0, heading=0)

psm_message.add_personal_safety_message(personal_safety_message)
psm_json = psm_message.to_json()

with open('psm.json', 'w', encoding='utf-8') as f:
  json.dump(psm_json, f, ensure_ascii=False, indent=4)

tim_message = TIM()
data_frame = DataFrame(frameType=TravelerInfoType.roadSignage,
                       msgID='\x68\x65\x6c\x6c\x6f',
                       startTime=0, durationTime=0, priority=0,
                       regions=[GeographicalPath(name=None, id=None, anchor=Position3D(lat=0, lon=0), laneWidth=None, closedPath=None, direction=None)],
                       content=Advisory(item=1234))
tim_message.add_data_frame(data_frame)
tim_json = tim_message.to_json()

with open('tim.json', 'w', encoding='utf-8') as f:
  json.dump(tim_json, f, ensure_ascii=False, indent=4)

rsa_message = RSA()
road_side_alert = RoadSideAlert(typeEvent=1, description=[1234], priority=None, heading=None, extent=None, position=None, furtherInfoID=None, regional=None)
rsa_message.add_road_side_alert(road_side_alert)
rsa_json = rsa_message.to_json()

with open('rsa.json', 'w', encoding='utf-8') as f:
  json.dump(rsa_json, f, ensure_ascii=False, indent=4)