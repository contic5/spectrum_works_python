import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
import copy

changingvalues=False
df = pd.read_csv("FIFA_World_Cup_Summary.csv")

champions=df["CHAMPION"].tolist()

uniquechampions=copy.deepcopy(champions)
uniquechampions=list(set(uniquechampions))

totalwins_list=[]
for i in range(len(uniquechampions)):
    totalwins=champions.count(uniquechampions[i])
    totalwins_list.append(totalwins)


#Scatterplot data and show it
plt.bar(uniquechampions,totalwins_list)
plt.show()