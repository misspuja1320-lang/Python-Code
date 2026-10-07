# wap to generated graph

import matplotlib.pyplot as plt
file=r"D:\PUJA MISHRA All Program\PYTHON\array.txt"
x=[]
y=[]
with open(file,"r") as f:
    for line in f:
        line=line.strip()
        if not line:
            continue
        a,b=line.split()
        x.append(float(a))
        y.append(float(b))
plt.plot(x,y,marker='*')
plt.xlable("x")
plt.ylable("y")
plt.title("graph")
plt.grid(True)
plt.show()