# Class of functions and objects that 
# TAKE: a destination; like Lions Arena
# her column for how far they are from the inputted destination (in dataframe) 
# you would have to check how far it is somehow using a library

import pandas as pd
from math import sqrt
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="MySpot")
df = pd.read_csv("df_with_coordinate.csv")
address_list = df["ADDRESS"].tolist()
LAT_DISTANCE = 110.574 #km
LONG_DISTANCE = 85 #km

distance_list = []

def distance(location):
  loc1 = geolocator.geocode(location)
  lat1 = loc1.latitude
  long1 = loc1.longitude
  #distance_list = []
  dis = float(0)
  count = int(0)
  for item in address_list:
    lat2 = df["LATTITUDE"][count]
    long2 = df["LONGITUDE"][count]
    dis = sqrt(pow(abs(lat1 - lat2)*LAT_DISTANCE,2) + pow(abs(long1 - long2)*LONG_DISTANCE,2))
    distance_list.append(dis)
    count += 1
  return distance_list
"""
df["DISTANCE"] =  distance("Lions Arena Kitchener")
print(df)
"""
