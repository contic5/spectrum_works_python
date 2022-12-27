import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

colornames=["blue","yellow","green","red","purple","brown"]
columnames=["facecream","facewash","toothpaste","bathingsoap","shampoo","moisturizer"]

df=pd.read_csv("company_sales_data.csv")

for i in range(len(colornames)):

    x=df["month_number"]
    y=df[columnames[i]]
    plt.plot(x,y,'o:',color=colornames[i],linewidth=3,label=columnames[i].capitalize()+" Sales df")
    plt.xticks(np.arange(min(x), max(x)+1, 1.0))
    #plt.ylim(100000,500000)
plt.legend(loc='upper left')
plt.title('Company Sales df of last year')
plt.show()