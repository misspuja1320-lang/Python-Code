# line graph using matplotlib for two array

import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[10,20,15,40,25]
plt.plot(x,y,marker='*')
plt.xlable("x")
plt.ylable("y")
plt.title("graph")
plt.grid(True)
plt.show()