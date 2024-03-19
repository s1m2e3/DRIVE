import geopandas as gpd
import numpy as np
from shapely.geometry import Point, Polygon
import json

class GeoFence():
    """
    GeoFence is the class that creates the geofence object capable of receiving coordinates and validating if 
    the coordinates fall inside the geofence.
    """    
    
    def __init__(self):
        self.geofences = []

    def add_geofences(self,filename:str):
        """
        add_geofences adds the geofences to the GeoFence object given a json configuration file

        :param filename: filename of the geofence configuration file, defaults to "config/GeoFences.json"
        :type filename: str, optional

        """
        with open(filename, 'r') as f:
            geofence_json = json.load(f)
        for geofence in geofence_json:
            polygon = []
            lats = []
            longs = []
            for point in (geofence['coordinates']):
                lats.append(point['lat'])
                longs.append(point['long'])
            polygon = Polygon(zip(longs, lats))
            polygon.id = geofence['id']
            self.geofences.append(polygon)    

    def in_geofence(self, lat:float, long:float):
        """
        in_geofence checks if the given coordinates are inside the geofence

        :param lat: latitude of the coordinates
        :type lat: float
        :param long: longitude of the coordinates
        :type long: float
        :return: True if the coordinates are inside the geofence, False otherwise

        """
        point = Point(long,lat)
        within = False
        geofence_id = None

        for polygon in self.geofences:
            if polygon.within(point):
                within = True
                geofence_id = polygon.id
                break

        return within,geofence_id
    