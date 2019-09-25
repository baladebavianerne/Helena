#!/usr/bin/env python
# coding: utf-8

# In[186]:



import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import dataclasses as dataclass
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.integrate import quad
import math

#A class is defined for reactants telling about the stoichometry and the concentration (jeg kan ik stave og magter ik kommentere på min 
#klamme lorte kode. den plankes senere)
class Reactant :
  def __init__(self, name1, coef, conc, order):
    self.name1 = name1
    self.coef = coef
    self.conc = conc
    self.order = order
reactant = [Reactant("Reactant A",1,0.8,2),
           Reactant("Reactant B",2,0.6,1),
           Reactant("Reactant C",6,0.88,0)]

#A class is defined for the products telling about the stoich
class Product :
  def __init__(self, name, coef, conc):
    self.name = name
    self.coef = coef
    self.conc = conc
product = [Product("Product C",1,0), 
           Product("Product D",2,0)]    



#A class for the reaction is defined containing the reaction rate constant, the conversion and the tank volume.
class Reactor :
  def __init__(self, k, X, V):
    self.k = k
    self.X = X
    self.V = V
    
#the reaction parameters are defined. 
reactor = Reactor(1.2,0.8,8)




#Now the limitted reactant is found by finding the lowest amount of substance by multiplying the concentration of
#of each substance with the tank volume
#here an empty list is created to later contain the initial amount of each substance
Amount = [];
for r in reactant:
    amount = r.conc/r.coef*reactor.V
    #now the initial amount is assign to the list Amount
    Amount.append(amount)
    #now the lowest initial amount of substance is found, which is the limitting amount
    Limit_amount = min(Amount)

#Now the stoich number to the limited amount is found in order to rearrange the reaction.
for r in reactant:
    if Limit_amount == r.conc/r.coef*reactor.V:
        #the reaction coefficient to the limitted reactant is defined
        limit_coef = r.coef 
        #and the amount of the limitted reactant is found
        limit_amount = r.conc * reactor.V

    
#The conversion is always related to the limitted reactant. 
#The ending amount is now calulated for each reactant as N_i = N_i0-coef/limit_coef * N_i0_limit* X
Amount_end_reactants = [];
Name_of_reactant = [];
for r in reactant:
    rend = r.conc*reactor.V-r.coef/limit_coef*limit_amount*reactor.X
    name1 = r.name1
    Amount_end_reactants.append(rend)
    Name_of_reactant.append(name1)
#The ending amount is now calculated for each product as N_i = N_i0+coef/limit_coef * N_i0_limit* X
    
Amount_end_products = [];
Name_of_product = [];
for p in product:
    pend = p.conc*reactor.V+p.coef/limit_coef*limit_amount*reactor.X
    name = p.name
    Amount_end_products.append(pend)
    Name_of_product.append(name)
    
    
#The end concentration of each reactant is printed 
for x in range(len(Amount_end_reactants)): 
    print('The concentration of ' +str(Name_of_reactant[x]) + ' is ' + str(Amount_end_reactants[x]/reactor.V))
#The end concentration of each product is printed 
for x in range(len(Amount_end_products)): 
    print('The concentration of ' +str(Name_of_product[x]) + ' is ' + str(Amount_end_products[x]/reactor.V))


#Now the reaction kinetics are looked into in order to plot the concentration profile.
Begin_amount = [];
order = [];
coef = [];
Begin_conc = [];
for r in reactant:
    begin_amount = r.conc*reactor.V
    begin_conc = r.conc
    Order = r.order
    Coef = r.coef
    #now the initial amount is assign to the list Amount
    Begin_amount.append(begin_amount)
    order.append(Order)
    coef.append(Coef)
    Begin_conc.append(begin_conc)
    

number_of_reactants = len(Begin_amount) 
    
def integrand(X):
    rate = 1
    for r in reactant:
        concentration =  r.conc - r.coef/limit_coef * limit_amount/reactor.V * X
        rate_per_reactant = concentration**r.order
        rate = rate * rate_per_reactant 
            
    return (limit_amount/reactor.V)/((reactor.k*rate))
t_reaction, err = quad(integrand, 0, reactor.X)
print(t_reaction)
    
    
    
    
def model(conc, reaction_time):
    rate1 = 1;
    for c in range(len(Begin_amount)):
        each = conc[c-1]**order[c-1]
        rate1 = rate1 * each
    dCdt = [];
    for r in reactant:
        ddCdt = -reactor.k * rate1 * r.coef /limit_coef 
        dCdt.append(ddCdt)
    return dCdt
    
reaction_time = np.linspace(0,t_reaction,num=600)
    
sol = odeint(model, Begin_conc , reaction_time)
    
fig = plt.figure()
ax = plt.subplot(111)
ax.plot(reaction_time,sol[:,0], label = 'Ca')
ax.plot(reaction_time,sol[:,1], label = 'Cb')
ax.plot(reaction_time,sol[:,2], label = 'Cc')
plt.title('Concentration profile of reactants')
ax.legend()
plt.show()




# In[187]:


sol


# In[168]:


sol


# In[18]:


reactant.order


# In[ ]:




