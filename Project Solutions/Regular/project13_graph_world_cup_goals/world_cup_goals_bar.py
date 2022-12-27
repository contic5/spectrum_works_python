import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

changingvalues=False
df = pd.read_csv("WorldCupMatches_Modified.csv")

game_goals=df["Total_Goals"].tolist()
for i in range(len(game_goals)):
    game_goals[i]=float(game_goals[i])

X=np.arange(0,max(game_goals)+1,1)
y=np.arange(0,max(game_goals)+1,1)

for i in range(len(game_goals)):
    goalindex=game_goals[i]
    y[goalindex]+=1

#Scatterplot data and show it
plt.bar(X,y)
plt.xticks(X)
plt.xlabel("Score")
plt.ylabel("Total Games")
plt.title("World Cup Goal Distribution")
plt.show()