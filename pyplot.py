# Graph

import matplotlib.pyplot as plt
import pandas as pd
file=r"D:\PUJA MISHRA All Program\PYTHON\array.xlsx"
df=pd.read_excel(file)
x=df.iloc[:,0]
y=df.iloc[:,1]
plt.scatter(x,y)
plt.xlable("x")
plt.ylable("y")
plt.title("graph")
plt.grid(True)
plt.show()