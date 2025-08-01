import numpy as np
import matplotlib.pyplot as plt

S = [[0,0], [1,0], [1,1], [0,1]]
S.append(S[0]) 


fig = plt.figure()
xs, ys = zip(*S) #create lists of x and y values


plt.figure()
plt.plot(xs,ys) 
plt.show() # 
