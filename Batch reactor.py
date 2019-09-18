#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[39]:



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
from scipy.integrate import quad
import math

#First the loading period is defined, meaning the period it takes to fill up the tank.
Tload = 16
#Then the conversion is defined
X= 0.9
#Then the reaction rate constant is defined
k=1.5

#Now the class is defined which contains the name of the inlet stream(s), the flow of the inlet stream(s), the concentration
#of the inlet stream(s).
class InletStreams:
  def __init__(self, nameofstream, Fi, Ci):
      self.nameofstream = nameofstream
      self.Fi = Fi
      self.Ci = Ci
      
#The data for each inlet stream is defined as objects
inletstreamA = InletStreams("Stream A", 8, 0.15)



#Now the volume of each inlet stream is defined as Volume=Flow*loading time
VA = inletstreamA.Fi*Tload
#As the loading period is finished, the reaction can occur
#The total volume in the tank is defined as the sum of the volume of each inlet stream
Vtot = VA
#The concentration of each speicies af the tank is loaded is:
Ca0 = inletstreamA.Ci*VA/Vtot



#Then the reaction occurs and the and concentration of each species is:
#The end concentration of A is
CA=Ca0*(1-X)
#The end concentration of B is
CB=Ca0*X

#The reaction time for the reaction is now calculated 
def integrand(X):
  return Ca0/(k*(1-X)*Ca0)

t_reaction, err = quad(integrand, 0, X)
print(ans)




#A vector is created ranging from 0.1 to the reaction time
t_reac= math.ceil(t_reaction)
time = np.arange(1,t_reac, 0.00020)

#A vector for the concentration profile is defined for the given reaction order
Cons_profile=Ca0*np.exp(-k*time)


#Now the concentration profile is plotted 
fig = plt.figure()
ax = plt.subplot(111)
ax.plot(time,Cons_profile, label = 'Concentration of A')
ax.legend()
plt.show()
#ax.plot(time,VB, label = 'Volume flow B')
#ax.plot(time,Vtot, label = 'Volume total flow')
#plt.title('Legend inside')




# Now the volume of each inlet stream and the total tank volume is plotted from t=1 to t=loading period 
#fig = plt.figure()
#ax = plt.subplot(111)
#ax.plot(time,VA, label = 'Volume flow A')
#ax.plot(time,VB, label = 'Volume flow B')
#ax.plot(time,Vtot, label = 'Volume total flow')
#plt.title('Legend inside')
#ax.legend()
#plt.show()

#As the loading period is finished, the reaction can occur




#The total end volume of each stream is calculated
#VAend = Tload*inletstreamA.Fi
#VBend = Tload*inletstreamB.Fi
#The total volume in the tank after the loading period is calcultated as the sum of the volume of each stream
#Vtotend=VAend + VBend

#The total concentration of each substance in the tank is calculated
#Ca = inletstreamA.Ci*VAend/Vtotend
#Cb = inletstreamB.Ci*VBend/Vtotend


#All of the values are printed
#print('The concentration of A is ' + repr(Ca) + ', and the concentration of B is ' + repr(Cb))
#print('The total volume in the tank is ' + repr(Vtotend))


# In[33]:


time


# In[35]:


Cons_profile


# In[ ]:


Ca0


# In[ ]:




