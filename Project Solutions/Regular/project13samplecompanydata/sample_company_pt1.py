import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("company_sales_data.csv")

x=df["month_number"]
y=df["total_profit"]
plt.plot(x,y)
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.ylim(100000,500000)
plt.show()