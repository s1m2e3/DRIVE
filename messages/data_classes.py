from dataclasses import dataclass
from enum import Enum
from typing import Union,List,Optional


class TravelerInfoType(Enum):

    unknown = 0
    advisory = 1
    roadSignage = 2
    comercialSignage = 3

class PersonalDeviceUserType(Enum):

    unavailable = 0
    aPEDESTRIAN = 1
    aPEDALCYCLIST = 2
    aPUBLICSAFETYWORKER = 3
    anANIMAL = 4   

class PriorityRequestType(Enum):

    priorityRequestTypeReserved = 0
    priorityRequest = 1
    priorityRequestUpdate = 2
    priorityCancellation = 3

class Extent(Enum):
    useInstantlyOnly = 0
    useFor3meters = 1
    useFor10meters = 2
    useFor50meters = 3
    useFor100meters = 4
    userFor500meters = 5
    useFor1000meters = 6
    useFor5000meters = 7
    useFor10000meters = 8
    useFor50000meters = 9
    useFor100000meters = 10
    useFor500000meters = 11
    useFor1000000meters = 12
    useFor5000000meters = 13
    useFor10000000meters = 14
    forever = 15

class TimeConfidence(Enum):
    unavailable = 0
    time_100_000 = 1
    time_050_000 = 2
    time_020_000 = 3
    time_010_000 = 4
    time_002_000 = 5
    time_001_000 = 6
    time_000_500 = 7
    time_000_200 = 8
    time_000_100 = 9
    time_000_050 = 10
    time_000_020 = 11
    time_000_010 = 12
    time_000_005 = 13
    time_000_002 = 14
    time_000_001 = 15
    time_000_000_5 = 16
    time_000_000_2 = 17
    time_000_000_1 = 18
    time_000_000_05 = 19
    time_000_000_02 = 20
    time_000_000_01 = 21
    time_000_000_005 = 22  
    time_000_000_002 = 23  
    time_000_000_001 = 24
    
class PositionConfidence(Enum):
    unavailable = 0
    a500m = 1
    a200m = 2
    a100m = 3
    a50m = 4
    a20m = 5
    a10m = 6
    a5m = 7
    a2m = 8
    a1m = 9
    a50cm = 10
    a20cm = 11
    a10cm = 12
    a5cm = 13
    a2cm = 14
    a1cm = 15

class ElevationConfidence(Enum):
    unavailable = 0
    elev_500_00 = 1
    elev_200_00 = 2
    elev_100_00 = 3
    elev_050_00 = 4
    elev_020_00 = 5
    elev_010_00 = 6
    elev_005_00 = 7
    elev_002_00 = 8
    elev_001_00 = 9
    elev_000_50 = 10
    elev_000_20 = 11
    elev_000_10 = 12
    elev_000_05 = 13
    elev_000_02 = 14
    elev_000_01 = 15
class HeadingConfidence(Enum):
    unavailable = 0
    prec10deg = 1
    prec05deg = 2
    prec01deg = 3
    prec0_1deg = 4
    prec0_05deg = 5
    prec0_01deg = 6
    prec0_0125deg = 7
class SpeedConfidence(Enum):
    unavailable = 0
    prec100m = 1
    prec10m = 2
    prec5m = 3
    prec1m = 4
    prec0_1m = 5
    prec0_05m = 6
    prec0_01m = 7
class ThrottleConfidence(Enum):
    unavailable = 0
    prec10percent = 1
    prec1percent = 2
    prec0_5percent = 3
@dataclass
class Position3D():
    lat: float
    lon: float
    
@dataclass
class RoadSignID():
    position: Position3D
    viewAngle: bytes
    
@dataclass
class RoadSegmentReferenceID():
    region: Optional[int]
    id: int
@dataclass
class GeographicalPath():
    name: Optional[str]
    id: Optional[RoadSegmentReferenceID]
    anchor: Optional[Position3D]
    laneWidth: Optional[int]
    closedPath: Optional[bool]
    direction: Optional[bytes]
@dataclass
class Advisory():
    item: Union[int,str]
@dataclass
class WorkZone():
    item: Union[int,str]
@dataclass 
class GenericSign():
    item: Union[int,str]
@dataclass
class SpeedLimit():
    item: Union[int,str]
@dataclass
class ExitService():
    item: Union[int,str]
@dataclass
class PositionalAccuracy():
    semiMajor: int
    semiMinor: int
    orientation: int

@dataclass
class FullPositionVector():
    utcTime: int
    long: int
    lat: int
    elevation: int
    heading: int
    speed: int
    posAccuracy: List[int,int,int]
    timeConfidence: TimeConfidence
    posConfidence: List[PositionConfidence,ElevationConfidence]
    speedConfidence: Optional[List[HeadingConfidence,SpeedConfidence, ThrottleConfidence]]