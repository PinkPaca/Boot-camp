import matplotlib.pyplot as plt
import numpy as np

#Prepare the data
x=np.linspace(0,100,100)
y=np.sin(x)
#Plot the data
plt.plot(x,y,label="sine")
#Create
plt.title("My first mataplotlib sine graph")

plt.show()