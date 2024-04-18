from dataclasses import dataclass
from enum import Enum
from typing import Union,List,Optional
import os

class TravelerInfoType(Enum):

    unknown = 0
    advisory = 1
    roadSignage = 2
    comercialSignage = 3
    def __post_init__(self):
        self.validate(self.value)
    def validate(self, value):
        if not isinstance(value, int) or value < 0 or value > 3:
            raise ValueError("value must be an integer between 0 and 3")
    def get_default(self):
        return TravelerInfoType.unknown.value

class PersonalDeviceUserType(Enum):

    unavailable = 0
    aPEDESTRIAN = 1
    aPEDALCYCLIST = 2
    aPUBLICSAFETYWORKER = 3
    anANIMAL = 4   
    def __post_init__(self):
        self.validate(self.value)
    def validate(self, value):
        if not isinstance(value, int) or value < 0 or value > 4:
            raise ValueError("value must be an integer between 0 and 4")
    def get_default(self):
        return PersonalDeviceUserType.unavailable.value


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
    def __post_init__(self):
        self.validate(self.value)
    def validate(self, value):
        if not isinstance(value, int) or value < 0 or value > 15:
            raise ValueError("value must be an integer between 0 and 15")
    def get_default(self):
        return Extent.useInstantlyOnly.value    
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
    def __post_init__(self):
        self.validate(self.value)
    def validate(self, value):
        if not isinstance(value, int) or value < 0 or value > 24:
            raise ValueError("value must be an integer between 0 and 24")
    def get_default(self):
        return TimeConfidence.unavailable.value
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
    def __post_init__(self):
        self.validate(self.value)
    def validate(self, value):
        if not isinstance(value, int) or value < 0 or value > 15:
            raise ValueError("value must be an integer between 0 and 15")
    def get_default(self):
        return PositionConfidence.unavailable.value
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
    def __post_init__(self):
        self.validate(self.value)
    def validate(self, value):
        if not isinstance(value, int) or value < 0 or value > 15:
            raise ValueError("value must be an integer between 0 and 15")
    def get_default(self):
        return ElevationConfidence.unavailable.value    
class HeadingConfidence(Enum):
    unavailable = 0
    prec10deg = 1
    prec05deg = 2
    prec01deg = 3
    prec0_1deg = 4
    prec0_05deg = 5
    prec0_01deg = 6
    prec0_0125deg = 7
    def __post_init__(self):
        self.validate(self.value)
    def validate(self, value):
        if not isinstance(value, int) or value < 0 or value > 7:
            raise ValueError("value must be an integer between 0 and 7")
    def get_default(self):
        return HeadingConfidence.unavailable.value
class HeadingSlice(Enum):
    from000_0to022_5degrees=0
    from022_5to045_0degrees=1
    from045_0to067_5degrees=2
    from067_5to090_0degrees=3
    from090_0to112_5degrees=4
    from112_5to135_0degrees=5
    from135_0to157_5degrees=6
    from157_5to180_0degrees=7
    from180_0to202_5degrees=8
    from202_5to225_0degrees=9
    from225_0to247_5degrees=10
    from247_5to270_0degrees=11
    from270_0to292_5degrees=12
    from292_5to315_0degrees=13
    from315_0to337_5degrees=14
    from337_5to360_0degrees=15

    def __post_init__(self):
        self.validate(self.value)

    def validate(self, value):
        if not isinstance(value, int) or value < 0 or value > 15:
            raise ValueError("value must be an integer between 0 and 15")
    def get_default(self):
        return HeadingSlice.from000_0to022_5degrees.value
class SpeedConfidence(Enum):
    unavailable = 0
    prec100m = 1
    prec10m = 2
    prec5m = 3
    prec1m = 4
    prec0_1m = 5
    prec0_05m = 6
    prec0_01m = 7
    def __post_init__(self):
        self.validate(self.value)
    def validate(self, value):
        if not isinstance(value, int) or value < 0 or value > 7:
            raise ValueError("value must be an integer between 0 and 7")
    def get_default(self):
        return SpeedConfidence.unavailable.value
class ThrottleConfidence(Enum):
    unavailable = 0
    prec10percent = 1
    prec1percent = 2
    prec0_5percent = 3
    def __post_init__(self):
        self.validate(self.value)
    def validate(self, value):
        if not isinstance(value, int) or value < 0 or value > 3:
            raise ValueError("value must be an integer between 0 and 3")
    def get_default(self):
        return ThrottleConfidence.unavailable.value

class TransmissionState(Enum):
    neutral = 0
    park = 1
    forwardGears = 2
    reverseGears = 3
    reserved1 = 4
    reserved2 = 5
    reserved3 = 6
    unavailable = 7
    def __post_init__(self):
        self.validate(self.value)
    def validate(self, value):
        if not isinstance(value, int) or value < 0 or value > 7:
            raise ValueError("value must be an integer between 0 and 7")
    def get_default(self):
        return TransmissionState.unavailable.value
class BrakeAppliedStatus(Enum):
    unavailable = 0
    leftFront = 1
    leftRear = 2
    rightFront = 3
    rightRear = 4
    def __post_init__(self):
        self.validate(self.value)
    def validate(self, value):
        if not isinstance(value, int) or value < 0 or value > 4:
            raise ValueError("value must be an integer between 0 and 4")
    def get_default(self):
        return BrakeAppliedStatus.unavailable.value
class TractionControlStatus(Enum):
    unavailable = 0
    off = 1
    on = 2
    engaged = 3
    def __post_init__(self):
        self.validate(self.value)
    def validate(self, value):
        if not isinstance(value, int) or value < 0 or value > 3:
            raise ValueError("value must be an integer between 0 and 3")
    def get_default(self):
        return TractionControlStatus.unavailable.value
class AntiLockBrakeStatus(Enum):
    unavailable = 0
    off = 1
    on = 2
    engaged = 3
    def __post_init__(self):
        self.validate(self.value)
    def validate(self, value):
        if not isinstance(value, int) or value < 0 or value > 3:
            raise ValueError("value must be an integer between 0 and 3")
    def get_default(self):
        return AntiLockBrakeStatus.unavailable.value    
class StabilityControlStatus(Enum):
    unavailable = 0
    off = 1
    on = 2
    engaged = 3
    def __post_init__(self):
        self.validate(self.value)
    def validate(self, value):
        if not isinstance(value, int) or value < 0 or value > 3:
            raise ValueError("value must be an integer between 0 and 3")
    def get_default(self):
        return StabilityControlStatus.unavailable.value
    
class brakeBoostApplied(Enum):
    unavailable = 0
    off = 1
    on = 2

    def __post_init__(self):
        self.validate(self.value)

    def validate(self, value):
        if not isinstance(value, int) or value < 0 or value > 2:
            raise ValueError("value must be an integer between 0 and 2")
    def get_default(self):
        return brakeBoostApplied.unavailable.value
class AuxiliaryBrakeStatus(Enum):
    unavailable = 0
    off = 1
    on = 2
    reserved = 3

    def __post_init__(self):
        self.validate(self.value)

    def validate(self, value):
        if not isinstance(value, int) or value < 0 or value > 3:
            raise ValueError("value must be an integer between 0 and 3")
    def get_default(self):
        return AuxiliaryBrakeStatus.unavailable.value

class Latitude():
    def validate(self, value):
        if not isinstance(value, int) or value < -900000000 or value > 900000001:
            raise ValueError("Latitude must be between -900000000 and 900000001")
    def get_default(self):
        return 900000001
class Longitude():
    def validate(self, value):
        if not isinstance(value, int) or value < -1800000001 or value > 1800000001:
            raise ValueError("Longitude must be between -1800000001 and 1800000001")
    def get_default(self):
        return 1800000001
class Elevation():
    def validate(self, value):
        if not isinstance(value, int) or value < -4096 or value > 61439:
            raise ValueError("Elevation must be between -4096 and 61439")
    def get_default(self):
        return -4096
class Heading():
    def validate(self, value):
        if not isinstance(value, int) or value < -0 or value > 28800:
            raise ValueError("Heading must be between -0 and 28800")
    def get_default(self):
        return 28800

class Velocity():
    def validate(self, value):
        if not isinstance(value, int) or value < 0 or value > 8191:
            raise ValueError("Velocity must be between 0 and 8191")
    def get_default(self):
        return 8191
@dataclass
class TransmissionAndSpeed():
    transmissionState: int = TransmissionState.get_default()
    speed: int = Velocity.get_default()

    def __post_init__(self):
        self._validate_inputs()
    def _validate_inputs(self):
        TransmissionState.validate(self.transmissionState)
        Velocity.validate(self.speed)

@dataclass
class Position3D():
    lat: int = Latitude.get_default()
    lon: int = Longitude.get_default

    def __post_init__(self):
        self._validate_inputs()

    def _validate_inputs(self):
        Latitude.validate(self.lat)
        Longitude.validate(self.lon)
        
@dataclass
class RoadSignID():
    position: Position3D = Position3D()
    viewAngle: int = HeadingSlice.get_default()

    def __post_init__(self):
        self._validate_inputs()

    def _validate_inputs(self):
        if not isinstance(self.position, Position3D):
            raise ValueError("position must be a Position3D object")
        if not isinstance(self.viewAngle, int):
            raise ValueError("view angle must be an integer")
        HeadingSlice.validate(self.viewAngle)
        self.position._validate_inputs()

class RoadRegulatorID():
    def validate(self, value):
        if not isinstance(value, int) or value < 0 or value > 65535:
            raise ValueError("value must be an integer between 0 and 65535")
    def get_default(self):
        return 65535
class RoadSegmentID():
    def validate(self, value):
        if not isinstance(value, int) or value < 0 or value > 65535:
            raise ValueError("value must be an integer between 0 and 65535")
    def get_default(self):
        return 65535

@dataclass
class RoadSegmentReferenceID():
    region: Optional[int] = RoadRegulatorID.get_default()
    id: int = RoadSegmentID.get_default()
    def __post_init__(self):
        self._validate_inputs()

    def _validate_inputs(self):
        RoadRegulatorID.validate(self.region)
        RoadSegmentID.validate(self.id)

class DescriptiveName():
    def validate(self, value):
        if not isinstance(value, str):
            raise ValueError("value must be a string")
    def get_default(self):
        return ""
class LaneWidth():
    def validate(self, value):
        if not isinstance(value, int) or value < 0 or value > 32767:
            raise ValueError("value must be an integer between 0 and 32767")
    def get_default(self):
        return 32767
@dataclass
class GeographicalPath():
    name: Optional[str] = DescriptiveName.get_default()
    id: Optional[RoadSegmentReferenceID] = RoadSegmentReferenceID()
    anchor: Optional[Position3D] = Position3D()
    laneWidth: Optional[int] = LaneWidth.get_default()
    closedPath: Optional[bool] = False
    direction: Optional[int] = HeadingSlice.get_default()

    def __post_init__(self):
        self._validate_inputs()

    def _validate_inputs(self):
        DescriptiveName.validate(self.name)
        self.id._validate_inputs()
        LaneWidth.validate(self.laneWidth)
        if not isinstance(self.closedPath, bool):
            raise ValueError("closedPath must be a boolean")
        HeadingSlice.validate(self.direction)

class ITISCodes():
    def validate(self, value):
        if not isinstance(value, int) or value < 0 or value > 65535:
            raise ValueError("value must be an integer between 0 and 65535")
    def get_default(self):
        return 65535
class ITIStextPhrase():
    def validate(self,value):
        if not isinstance(value, str):
            raise ValueError("value must be a string")
        if len(value)>17:
            raise ValueError("value must be less than 17 characters")
    def get_default(self):
        return ""
class Item():
    itis : int = ITISCodes.get_default()
    text : str = None
    def __post_init__(self):
        self._validate_inputs()

    def _validate_inputs(self):
        if isinstance(self.itis, int) and self.text is None:
            ITISCodes.validate(self.itis)
        elif isinstance(self.text, str) and self.itis is None:
            ITIStextPhrase.validate(self.text)
        elif isinstance(self.itis, int) and isinstance(self.text, str):
            ITISCodes.validate(self.itis)
        
@dataclass
class ITIScodesAndText():
    item: List[Item] = []
    def __post_init__(self):
        self._validate_inputs()

    def _validate_inputs(self):
        if not isinstance(self.item, list):
            raise ValueError("item must be a list")
        if len(self.item)>100:
            raise ValueError("item must be less than 100 items")
        for item in self.item:
            item._validate_inputs()

@dataclass
class WorkZone(ITIScodesAndText):
    def __post_init__(self):
        super().__post_init__()
    def _validate_inputs(self):
        super()._validate_inputs()
        if len(self.item)>16:
            raise ValueError("item must be less than 16 items")
@dataclass
class GenericSignage(WorkZone):
    def __post_init__(self):
        super().__post_init__()
@dataclass
class SpeedLimit(WorkZone):
    def __post_init__(self):
        super().__post_init__()
@dataclass
class ExitService(WorkZone):
    def __post_init__(self):
        super().__post_init__()

@dataclass
class Content:
    advisory : ITIScodesAndText = ITIScodesAndText()
    workzone : WorkZone = None
    genericSign: GenericSignage = None
    speedLimit: SpeedLimit = None
    exitService: ExitService = None
    def __post_init__(self):
        self._validate_inputs()

    def _validate_inputs(self):
        num_not_none = sum(field is not None for field in
                           (self.advisory, self.workzone, self.genericSign,
                            self.speedLimit, self.exitService))
        if num_not_none != 1:
            raise ValueError("Only one of advisory, workzone, genericSign, "
                             "speedLimit, exitService can be not None at the "
                             "time")
        not_none_field = [field for field in (self.advisory, self.workzone,self.genericSign,self.speedLimit,self.exitService) if field is not None]
        not_none_field[0]._validate_inputs()

class SemiMajorAxisAccuracy():
    def validate(self, value):
        if not isinstance(value, int) or value < 0 or value > 255:
            raise ValueError("value must be an integer between 0 and 255")
    def get_default(self):
        return 255
class SemiMinorAxisAccuracy(SemiMajorAxisAccuracy):
    pass

class SemiMajorAxisOrientation():
    def validate(self,value):
        if not isinstance(value, int) or value < 0 or value > 65535:
            raise ValueError("value must be an integer between 0 and 65535")
    def get_default(self):
        return 65535
    
@dataclass
class PositionalAccuracy():
    semiMajor: int = SemiMajorAxisAccuracy.get_default()
    semiMinor: int = SemiMinorAxisAccuracy.get_default()
    orientation: int = SemiMajorAxisOrientation.get_default()
    def __post_init__(self):
        self._validate_inputs()

    def _validate_inputs(self):
        SemiMajorAxisAccuracy.validate(self.semiMajor)
        SemiMinorAxisAccuracy.validate(self.semiMinor)
        SemiMajorAxisOrientation.validate(self.orientation)

@dataclass
class PositionConfidenceSet():
    pos : int = PositionConfidence.get_default()
    elevation : int = ElevationConfidence.get_default()
    def __post_init__(self):
        self._validate_inputs()

    def _validate_inputs(self):
        PositionConfidence.validate(self.pos)
        ElevationConfidence.validate(self.elevation)

@dataclass
class SpeedandHeadingandThrottleConfidence():
    heading: int = HeadingConfidence.get_default()
    speed: int = SpeedConfidence.get_default()
    throttle: int = ThrottleConfidence.get_default()

    def __post_init__(self):
        self._validate_inputs()

    def _validate_inputs(self):
        HeadingConfidence.validate(self.heading)
        SpeedConfidence.validate(self.speed)
        ThrottleConfidence.validate(self.throttle)

@dataclass
class FullPositionVector():
    long: int = Longitude.get_default()
    lat: int = Latitude.get_default()
    elevation: int = Elevation.get_default()
    heading: int = Heading.get_default()
    speed: TransmissionAndSpeed = TransmissionAndSpeed()
    posAccuracy: PositionalAccuracy = PositionalAccuracy()
    timeConfidence: int = TimeConfidence.get_default()
    posConfidence: PositionConfidenceSet = PositionConfidenceSet()
    speedConfidence: SpeedandHeadingandThrottleConfidence = SpeedandHeadingandThrottleConfidence()

    def __post_init__(self):
        self._validate_inputs()

    def _validate_inputs(self):
        
        Longitude.validate(self.long)
        Latitude.validate(self.lat)
        Elevation.validate(self.elevation)
        Heading.validate(self.heading)
        TransmissionAndSpeed._validate_inputs(self.speed)
        PositionalAccuracy._validate_inputs(self.posAccuracy)
        TimeConfidence.validate(self.timeConfidence)
        PositionConfidenceSet._validate_inputs(self.posConfidence)
        SpeedandHeadingandThrottleConfidence._validate_inputs(self.speedConfidence)

@dataclass
class AccelerationSet4Way():
    long: int = 2001
    lat: int = 2001
    vert: int = -127
    yaw: int = 0
    def __post_init__(self):
        self._validate_input()

    def _validate_input(self):
        if not isinstance(self.long, int) or self.long < -2000 or self.long > 2001:
            raise ValueError("long must be an int within the range [-2000, 2001]")
        if not isinstance(self.lat, int) or self.lat < -2000 or self.lat > 2001:
            raise ValueError("lat must be an int within the range [-2000, 2001]")
        if not isinstance(self.vert, int) or self.vert < -127 or self.vert > 127:
            raise ValueError("vert must be an int within the range [-127, 127]")
        if not isinstance(self.yaw, int) or self.yaw < -32767 or self.yaw > 32767:
            raise ValueError("yaw must be an int within the range [-32767, 32767]")


@dataclass
class BrakeSystemStatus():
    wheelBrakes: int = BrakeAppliedStatus.unavailable.value
    traction: int = TractionControlStatus.unavailable.value
    abs: int = AntiLockBrakeStatus.unavailable.value
    scs: int = StabilityControlStatus.unavailable.value
    brakeBoost: int = brakeBoostApplied.unavailable.value
    auxBrakes:int = AuxiliaryBrakeStatus.unavailable.value
    def __post_init__(self):
        self._validate_input()

    def _validate_input(self):
        if not isinstance(self.wheelBrakes, int) or self.wheelBrakes < BrakeAppliedStatus.unavailable.value or self.wheelBrakes > BrakeAppliedStatus.max_value:
            raise ValueError("wheelBrakes must be an integer between BrakeAppliedStatus.unavailable.value and BrakeAppliedStatus.max_value")
        if not isinstance(self.traction, int) or self.traction < TractionControlStatus.unavailable.value or self.traction > TractionControlStatus.max_value:
            raise ValueError("traction must be an integer between TractionControlStatus.unavailable.value and TractionControlStatus.max_value")
        if not isinstance(self.abs, int) or self.abs < AntiLockBrakeStatus.unavailable.value or self.abs > AntiLockBrakeStatus.max_value:
            raise ValueError("abs must be an integer between AntiLockBrakeStatus.unavailable.value and AntiLockBrakeStatus.max_value")
        if not isinstance(self.scs, int) or self.scs < StabilityControlStatus.unavailable.value or self.scs > StabilityControlStatus.max_value:
            raise ValueError("scs must be an integer between StabilityControlStatus.unavailable.value and StabilityControlStatus.max_value")
        if not isinstance(self.brakeBoost, int) or self.brakeBoost < brakeBoostApplied.unavailable.value or self.brakeBoost > brakeBoostApplied.max_value:
            raise ValueError("brakeBoost must be an integer between brakeBoostApplied.unavailable.value and brakeBoostApplied.max_value")
        if not isinstance(self.auxBrakes, int) or self.auxBrakes < AuxiliaryBrakeStatus.unavailable.value or self.auxBrakes > AuxiliaryBrakeStatus.max_value:
            raise ValueError("auxBrakes must be an integer between AuxiliaryBrakeStatus.unavailable.value and AuxiliaryBrakeStatus.max_value")
        

@dataclass 
class VehicleSize():
    width: int = 0
    length: int = 0
    def __post_init__(self):
        self._validate_input()

    def _validate_input(self):
        if not isinstance(self.width, int) or self.width < 0 or self.width > 1023:
            raise ValueError("width must be within the range [0, 1023]")
        if not isinstance(self.length, int) or self.length < 0 or self.length > 4095 :
            raise ValueError("length must be withing the range [0, 4095]")

@dataclass
class BSMcoreData():
    msgCnt: int = 0
    id: int = 99999999
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
        self._validate_input()
    def _validate_input(self):
        """
        Validate inputs, raise a ValueError if there is an invalid input.
        """
        
        if self.speed < 0 or self.speed > 8191:
            raise ValueError("Speed must be between 0 and 8191")
    
        if self.elev < -4096 or self.elev > 61439:
            raise ValueError("Elevation must be between -4096 and 61439")
    
        if self.angle < 0 or self.angle > 28800:
            raise ValueError("Angle must be between 0 and 28800")
    
        if self.lat < -900000000 or self.lat > 900000001:
            raise ValueError("Latitude must be between -900000000 and 900000001")
    
        if self.long < -1799999999 or self.long > .1800000001:
            raise ValueError("Longitude must be between -1799999999 and .1800000001")
    
        if self.secMark < 0 or self.secMark > 65535:
            raise ValueError("Second Mark must be between 0 and 2000000000")
    
        if self.msgCnt < 0 or self.msgCnt > 127:
            raise ValueError("Message Count must be between 0 and 127")
    
        if self.id < 0 or self.id > 10000000:
            raise ValueError("ID must be between 0 and 10000000")
        
        values = [member.value for member in TransmissionState]
        if not isinstance(self.transmission, int) or self.transmission < min(values) or self.transmission > max(values):
            raise ValueError("Transmission must be an integer between TransmissionState.unavailable.value and TransmissionState.max_value")
        
    

@dataclass
class DataFrame:
    frameType: TravelerInfoType
    msgID: Union[bytes, RoadSignID]
    startTime : int
    durationTime : int
    priority: int
    regions: List[GeographicalPath]
    content: Content
@dataclass
class BasicSafetyMessage():
    coreData : BSMcoreData = BSMcoreData()
@dataclass
class RoadSideAlert:
    typeEvent: int
    description: List[int]
    priority: Optional[bytes]
    heading : Optional[bytes]
    extent : Optional[Extent]
    position : Optional[FullPositionVector]
    furtherInfoID : bytes
    regional : Optional[List[dict]]

    

    

