from dataclasses import dataclass
from enum import Enum
from typing import Union
from typing import Optional

class TravelerInfoType(Enum):
    unknown = 0
    advisory = 1
    roadSignage = 2
    comercialSignage = 3

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
