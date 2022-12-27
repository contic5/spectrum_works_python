import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("company_sales_data.csv")

x=df["month_number"]
y=df["facewash"]
y2=df["facecream"]
barwidth=0.25

plt.bar([a-barwidth/2 for a in x],y,color="red",width=barwidth,label="Face Wash")
plt.bar([a+barwidth/2 for a in x],y2,color="blue",width=barwidth,label="Face Cream")
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.title('Sales data')
plt.grid(True, linewidth= 1, linestyle="--")

plt.legend(loc='upper left')
plt.title('Company Sales of Mouthwash vs Facecream')
plt.title('Facewash and facecream sales data')
plt.show()