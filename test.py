import pandas as pd
import distance
df = pd.read_csv("final.csv")
class Destination (object):
  def __init__(self,location):
    self.loc = location
  def result(self):
    df["DISTANCE"] = distance.distance(self.loc)
    print (df)
x = Destination("Lions Arena Kitchener")
x.result()