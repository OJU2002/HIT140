#for producing the histogram we have to import matplotlib.pyplot 
import pandas as pd
import matplotlib.pyplot as plt
#then we should get the data of fairfield which we named as assessment into python script
df = pd.read_csv("Assessment.csv")
sample = df.Mercury.values
#we have make the bins with 0.1 
max_val = sample.max()
min_val = sample.min()
the_range = max_val - min_val
bin_width = 0.1
bin_count = int(the_range / bin_width)
#inorder to plot histogram 
plt.hist(sample, color='green', edgecolor='black', bins=bin_count)
plt.title("Historgram for fairfield data")
plt.xlabel("value of Mercury")
plt.ylabel("Number of reserviour")
plt.show()