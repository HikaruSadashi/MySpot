# Class of functions and objects that 
# TAKE: a destination; like Lions Arena
# her column for how far they are from the inputted destination (in dataframe) 
# you would have to check how far it is somehow using a library

import pandas as pd
import numpy as np
from math import sqrt
from math import cos
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="MySpot")

"""
location1 = geolocator.geocode("161 University Avenue West, Waterloo")
location2 = geolocator.geocode("150 Pioneer Drive, Kitchener")
"""

df = pd.read_csv("Parking_Public_Lots_Merged.csv)

def distance(userInput, parkingLot):
  loc1 = geolocator.geocode(str(userInput))
  loc2 = geolocator.geocode(str(parkingLot))
  lat1 = loc1.latitude
  lat2 = loc2.latitude
  long1 = loc1.longitude
  long2 = long1.longitude

  dis = float(0)
  LAT_DISTANCE = 110.574 #km
  LONG_DISTANCE = 85 #km
  dis = sqrt(pow(abs(lat1 - lat2)*LAT_DISTANCE,2) + pow(abs(long1 - long2)*LONG_DISTANCE,2))
  return dis



  

