from dataclasses import dataclass
from enum import Enum
from typing import Union,List,Optional
import os

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
class TransmissionState(Enum):
    neutral = 0
    park = 1
    forwardGears = 2
    reverseGears = 3
    reserved1 = 4
    reserved2 = 5
    reserved3 = 6
    unavailable = 7

class BrakeAppliedStatus(Enum):
    unavailable = 0
    leftFront = 1
    leftRear = 2
    rightFront = 3
    rightRear = 4

class TractionControlStatus(Enum):
    unavailable = 0
    off = 1
    on = 2
    engaged = 3

class AntiLockBrakeStatus(Enum):
    unavailable = 0
    off = 1
    on = 2
    engaged = 3

class StabilityControlStatus(Enum):
    unavailable = 0
    off = 1
    on = 2
    engaged = 3

class brakeBoostApplied(Enum):
    unavailable = 0
    off = 1
    on = 2

class AuxiliaryBrakeStatus(Enum):
    unavailable = 0
    off = 1
    on = 2
    reserved = 3

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
    semiMajor: int = 255
    semiMinor: int = 255
    orientation: int = 65535

@dataclass
class PositionConfidenceSet():
    pos : PositionConfidence
    elevation : ElevationConfidence
@dataclass
class SpeedandHeadingandThrottleConfidence():
    heading: HeadingConfidence
    speed: SpeedConfidence
    throttle: ThrottleConfidence
@dataclass
class FullPositionVector():
    utcTime: int
    long: int
    lat: int
    elevation: int
    heading: int
    speed: int
    posAccuracy: PositionalAccuracy
    timeConfidence: TimeConfidence
    posConfidence: PositionConfidenceSet
    speedConfidence: SpeedandHeadingandThrottleConfidence
@dataclass
class AccelerationSet4Way():
    long: int = 2001
    lat: int = 2001
    vert: int = -127
    yaw: int = 0
@dataclass
class BrakeSystemStatus():
    wheelBrakes: int = BrakeAppliedStatus.unavailable.value
    traction: int = TractionControlStatus.unavailable.value
    abs: int = AntiLockBrakeStatus.unavailable.value
    scs: int = StabilityControlStatus.unavailable.value
    brakeBoost: int = brakeBoostApplied.unavailable.value
    auxBrakes:int = AuxiliaryBrakeStatus.unavailable.value

@dataclass 
class VehicleSize():
    width: int = 0
    length: int = 0
@dataclass
class BSMcoreData():
    msgCnt: int = 0
    id: int = int
    secMark: int = 65535
    lat: int  = 900000001
    long: int = 1800000001
    elev: int = -4096
    accuracy: PositionalAccuracy = PositionalAccuracy()
    transmission: int = TransmissionState.unavailable.value
    speed: int = 8191
    heading: int = 28800
    angle: int = 127
    accelSet: AccelerationSet4Way = AccelerationSet4Way()
    brakes: BrakeSystemStatus = BrakeSystemStatus()
    size: VehicleSize = VehicleSize()

    def __post_init__(self):
        """
        After the init method, validate each attribute to ensure they are of the correct type.
        """
        for attr, value in vars(self).items():
            if not isinstance(getattr(self, attr), type(value)):
                raise TypeError(f"{attr} must be of type {type(value)}")
    
    def _validate_input(self):
        """
        Validate inputs, raise a ValueError if there is an invalid input.
        """
        for attr, value in vars(self).items():
            if not isinstance(getattr(self, attr), type(value)):
                raise ValueError(f"{attr} must be of type {type(value)}")
    
        if self.speed < 0:
            raise ValueError("Speed cannot be negative")
    
        if self.elev < 0:
            raise ValueError("Elevation cannot be negative")
    
        if self.angle < 0 or self.angle > 28800:
            raise ValueError("Angle must be between 0 and 28800")
    
        if self.lat < -9000000 or self.lat > 9000000:
            raise ValueError("Latitude must be between -9000000 and 9000000")
    
        if self.long < -18000000 or self.long > 18000000:
            raise ValueError("Longitude must be between -18000000 and 18000000")
    
        if self.secMark < 0 or self.secMark > 2000000000:
            raise ValueError("Second Mark must be between 0 and 2000000000")
    
        if self.msgCnt < 0 or self.msgCnt > 127:
            raise ValueError("Message Count must be between 0 and 127")
    
        if self.size.width < 0 or self.size.width > 127:
            raise ValueError("Width must be between 0 and 127")
    
        if self.size.length < 0 or self.size.length > 127:
            raise ValueError("Length must be between 0 and 127")
    
        if self.accelSet.long < -32767 or self.accelSet.long > 32767:
            raise ValueError("Long Acceleration must be between -32767 and 32767")
    
        if self.accelSet.lat < -32767 or self.accelSet.lat > 32767:
            raise ValueError("Lat Acceleration must be between -32767 and 32767")
    
        if self.accelSet.vert < -32767 or self.accelSet.vert > 32767:
            raise ValueError("Vert Acceleration must be between -32767 and 32767")
    
        if self.accelSet.yaw < -32767 or self.accelSet.yaw > 32767:
            raise ValueError("Yaw Acceleration must be between -32767 and 32767")
    
        if self.brakes.wheelBrakes < 0 or self.brakes.wheelBrakes > 4:
            raise ValueError("Wheel Brakes must be between 0 and 4")
    
        
    
    

    
    

    

