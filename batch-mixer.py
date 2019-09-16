#!/usr/bin/env python
# coding: utf-8

# In[15]:


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 10:25:56 2019

@author: Helena Thøgersen, s153095
#Model for batch mixing
"""
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
inletstreamA = InletStreams("Stream A", 8, 0.15)
inletstreamB = InletStreams("StreamB", 6, 1.3)

#Now a time array is created with the length of the loading period.
time = np.arange(1,Tload)
#Now the volume of each inlet stream is defined as Volume=Flow*time
VA = inletstreamA.Fi*time
VB = inletstreamB.Fi*time

#The total volume in the tank is defined as the sum of the volume of each inlet stream
Vtot = VA + VB

# Now the volume of each inlet stream and the total tank volume is plotted from t=1 to t=loading period 
fig = plt.figure()
ax = plt.subplot(111)
ax.plot(time,VA, label = 'Volume flow A')
ax.plot(time,VB, label = 'Volume flow B')
ax.plot(time,Vtot, label = 'Volume total flow')
plt.title('Legend inside')
ax.legend()
plt.show()

#The total end volume of each stream is calculated
VAend = Tload*inletstreamA.Fi
VBend = Tload*inletstreamB.Fi
#The total volume in the tank after the loading period is calcultated as the sum of the volume of each stream
Vtotend=VAend + VBend

#The total concentration of each substance in the tank is calculated
Ca = inletstreamA.Ci*VAend/Vtotend
Cb = inletstreamB.Ci*VBend/Vtotend


#All of the values are printed
print('The concentration of A is ' + repr(Ca) + ', and the concentration of B is ' + repr(Cb))
print('The total volume in the tank is ' + repr(Vtotend))




# In[10]:


VAend


# In[8]:


Cb


# In[9]:


Ca


# In[ ]:




