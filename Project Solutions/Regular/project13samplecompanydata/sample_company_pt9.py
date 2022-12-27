import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

columnames=["Face Cream","Face Wash","Toothpaste","Bathing Soap","Shampoo","Moisturizer"]

df=pd.read_csv("company_sales_data.csv")

x=df["month_number"]
y0=df["bathingsoap"]
y1=df["facewash"]

plt.figure(figsize=(3, 6))

plt.subplot(2,1,1)
plt.plot(x, y0)
plt.subplot(2,1,2)
plt.plot(x, y1)
plt.suptitle('Categorical Plotting')
plt.show()