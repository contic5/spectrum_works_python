import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("company_sales_data.csv")

x=df["month_number"]
y=df["bathingsoap"]

plt.bar(x,y)
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.title('Sales data')
plt.grid(True, linewidth= 1, linestyle="--")

plt.title('Company Sales of Bathing Soap')
plt.show()