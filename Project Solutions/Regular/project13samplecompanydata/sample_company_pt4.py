from re import X
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("company_sales_data.csv")

x  = df ['month_number'].tolist()
y = df ['toothpaste'].tolist()
plt.scatter(x, y, label = 'Tooth paste Sales data')

#plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.legend(loc='lower right')
plt.title('Company Sales data of last year')
plt.show()