# import the dataset and pandas library
import pandas as pd
import distance
df = pd.read_csv("final.csv")
class Destination (object):
  def __init__(self,location):
    self.loc = location
  def result(self):
    df["DISTANCE"] = distance.distance(self.loc)
    return df
  def occupied(self, lot):
    count = df.index[df["ADDRESS"]==lot]
    if type(df['NUM_SPACES'][count]) != type(1):
      print ("Spaces information unavailable for this parking lot")
    else:
      df['NUM_SPACES'][count] = df['NUM_SPACES'][count] -1
    return df
  def left(self, lot):
    count = df.index[df["ADDRESS"]==lot]
    if type(df['NUM_SPACES'][count]) != type(1):
      print ("Spaces information unavailable for this parking lot")
    else:
      df['NUM_SPACES'][count] = df['NUM_SPACES'][count] +1
    return df
        
# sort the whole dataframe based on lowest (closest) distance values to biggest ones
a = Destination(input("Enter destination: "))
a.result()
df = df.sort_values(by=['DISTANCE'], kind= 'mergesort')
df = df[['NUM_SPACES', 'ADDRESS', 'LOCATION_DESCRIPTION','PARKING_COST', 'PAYMENT_METHOD', 'HOURS', 'DAYS', 'DISTANCE' ]]
print(df)

# marks the chosen spot occupied
a.occupied(input("Enter parking lot to arrive: ").upper())
print(df)

# unmark the spot 
a.left(input("Enter parking lot to leave: ").upper())
