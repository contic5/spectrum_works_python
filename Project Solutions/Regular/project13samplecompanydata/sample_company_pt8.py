import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

columnames=["Face Cream","Face Wash","Toothpaste","Bathing Soap","Shampoo","Moisturizer"]

df=pd.read_csv("company_sales_data.csv")
#Columns 1-6 by index

sums=df.sum(axis=0)
sums=sums[1:7]

plt.pie(sums,autopct='%1.1f%%',labels=columnames,startangle=90)
plt.title('Company Sales')
plt.show()