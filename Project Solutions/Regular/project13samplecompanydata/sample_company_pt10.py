import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

colornames=["blue","yellow","green","red","purple","brown"]
columnames=["facecream","facewash","toothpaste","bathingsoap","shampoo","moisturizer"]

df=pd.read_csv("company_sales_data.csv")

x=df["month_number"].tolist()
y=[]
for i in range(len(colornames)):
    nextpart=df[columnames[i]].tolist()
    y.append(nextpart)
   
plt.stackplot(x,y,labels=columnames)
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.legend(loc='upper left')
plt.title('Company Sales df of last year')
plt.show()