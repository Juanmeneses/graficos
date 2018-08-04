from pylab import *
import matplotlib.pyplot as plt
import numpy as np
from random import *

lis1 =[1,2,3,4,5,6,]
lis2 =[12,14,16,18,20,14] 
lis3 =[32,2,5,7,9,2,45]

plt.ylabel("eje Y")
plt.xlabel("eje X")
plt.plot(lis1, marker='o',linestyle=':',color = 'blue',label='enero')
plt.plot(lis2, marker='+',linestyle='--',label='febrero',color = 'red')
plt.plot(lis3,marker='*',linestyle = '-.', label = 'marzo',color='brown')
plt.legend(loc="upper center")
plt.show()
