#Hit140 #group19 #Assessment 1
#first we have to import pandas and matplotlib.pyploy so we can read the fairfield data
   
from re import X
import pandas as pd
import matplotlib.pyplot as plt

# then we should get the data of fairfield which we named as assessment into python script
# we haave to read the fairfield data using pandas
# we have named the fairfield data as Assessment.cvs
df = pd.read_csv("Assessment.csv")
print(df.describe())
#seperate mercury value can be obtain
print(df["Mercury"].describe())