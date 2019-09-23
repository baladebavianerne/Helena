#!/usr/bin/env python
# coding: utf-8

# In[1]:



#@author: Helena Thøgersen, s153095
#Model for batch mixing

#initialization
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import dataclasses as dataclass
import matplotlib.pyplot as plt


#First the loading period is defined, meaning the period it takes to fill up the tank.
Tload = 16

#Now the class is defined which contains the name of the inlet stream(s), the flow of the inlet stream(s) and the concentration
#of the inlet stream(s).
class InletStreams:
    def __init__(self, nameofstream, Fi, Ci):
        self.nameofstream = nameofstream
        self.Fi = Fi
        self.Ci = Ci
        
#The data for each inlet stream as objects
inletstreams = [InletStreams("Stream A", 8, 0.15),
                InletStreams("StreamB", 6, 0.3)]

#Now a time array is created with the length of the loading period.
time = np.arange(1,Tload)
#Now the volume of each inlet stream is defined as Volume=Flow*time


Volume_stream = [];
for i in inletstreams:
    V = i.Fi * time
    Volume_stream.append(V)
    
Vtot = sum(Volume_stream)

fig = plt.figure()
ax = plt.subplot(111)
ax.plot(time,Vtot, label = 'Total volume')
plt.title('Legend inside')
ax.legend()
plt.show()


for x in inletstreams:
    print('The concenctration of ' + repr(x.nameofstream) + ' is ' + repr(x.Ci*x.Fi*Tload/Vtot[-1]) )

#All of the values are printed
#print('The concentration of A is ' + repr(Ca) + ', and the concentration of B is ' + repr(Cb))
#print('The total volume in the tank is ' + repr(Vtotend))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




