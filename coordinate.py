import pandas as pd
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="MySpot")
df = pd.read_csv("Parking_Public_Lots_Merged_Updated.csv")
address_list = df["ADDRESS"].tolist()
lat_list = []
long_list = []

def export_lat(addresses):
  loc = ""
  for item in addresses:
    loc = geolocator.geocode(item)
    lat = loc.latitude
    lat_list.append(lat)
  return lat_list
df["LATTITUDE"] = export_lat(address_list)
print (df["LATTITUDE"])

def export_long(addresses):
  loc = ""
  for item in addresses:
    loc = geolocator.geocode(item)
    long = loc.longitude
    long_list.append(long)
  return long_list
df["LONGITUDE"] = export_long(address_list)
print (df["LONGITUDE"])
df.to_csv("Complete df.csv")
  
