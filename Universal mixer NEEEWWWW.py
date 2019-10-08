#!/usr/bin/env python
# coding: utf-8

# In[127]:


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
class InletComponent:
    def __init__(self, nameofcomp, Xi, amount, startamount):
        self.nameofcomp = nameofcomp
        self.Xi = Xi
        self.amount = amount
        self.startamount = startamount
        
       
#The data for each inlet stream as objects
inletcomponents = [InletComponent("invert sugars", 0.025, 125, 'X'),
                   InletComponent("water", 0.5, 125, 'X'),
                  InletComponent("solids", 0.475, 125, 'X'),
                  InletComponent("invert sugars", 0.01, 45, 'X'),
                  InletComponent("water", 0.18, 45, 'X'),
                  InletComponent("solids", 0.31, 45, 'X'),
                  InletComponent("sucrose", 0.5, 45, 'X'),
                  InletComponent("water", 1, 8.75, 'X')]

#start amount for each species in batch reactor is found as the fraction times the total amount of inlet stream
components  = [];
startamounts = [];
for i in inletcomponents:
    i.startamount = i.Xi*i.amount
    components.append(i.nameofcomp)
    startamounts.append(i.startamount)

#but some of the substances occur in multiple streams. Therefor it is found with substances occur multiple times.
#this list is defines to contain the information of the actual start amount, with is the sum of the different 
#amount of species in the different streams
actual_begin_amount = [];
for i in inletcomponents:
    #this function tells the index of where each substance occurs. 
    get_indexes = lambda components, xs: [i for (y, i) in zip(xs, range(len(xs))) if components == y]
    indexes = get_indexes(i.nameofcomp,components)
   #this list is defined to contain information about the amount of substance for each species in each stream
    a = [0]*len(indexes)
    
    for i in range(len(a)):
        ind = indexes[i-1]
        #now the amount of substance for each stream it occurs in is storred in the list a.
        a[i-1] = startamounts[ind]
        #now the sum is found of each substance in order to find the total amount of substance of each substance
        b= sum(a)
    #the information about the total amount is storred in the following list  
    actual_begin_amount.append(b)
    
#now some of the amounts/names occurs muktible times, with the same amount and components name which just makes it
#a repitition and therefore it can be deleted.
name = [];
amount_begin = [];
end_frac = [];
    
for i in range(len(components)):
    #if the component already is storred, then it has to just throw it away
    if components[i] in name:
        hej = 2
    #if it has not been storred, it has to be saved in the list
    else:
        name.append(components[i])
        amount_begin.append(actual_begin_amount[i])
    
#finding the ending fraction of each component which is done by amount of substance/total amount *100
totalamount = sum(amount_begin)
end_frac = [];
for i in range(len(amount_begin)):
    end = amount_begin[i-1]/totalamount*100
    end_frac.append(end)

#now the information is printet   
for i in range(len(amount_begin)): 
    print('The beginning amount' +str(name[i]) + ' is ' + str(amount_begin[i]) + ' and the end massfraction is ' + str(end_frac[i]))    


# In[124]:


amount_begin


# In[114]:


amount_begin


# In[125]:


end_frac


# In[3]:





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




