import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("company_sales_data.csv")

x=df["month_number"]
profitList = df ['total_profit'].tolist()
profit_range = [150000, 175000, 200000, 225000, 250000, 300000, 350000]

plt.hist(profitList,profit_range,label="Profit Data")

plt.title('Company Sales')
plt.show()