#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[90]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import dataclasses as dataclass
import matplotlib.pyplot as plt
from scipy.integrate import quad
import math

#A class is defined for reactants telling about the stoichometry and the concentration (jeg kan ik stave og magter ik kommentere på min 
#klamme lorte kode. den plankes senere)
class Reactant :
  def __init__(self, name1, coef, conc):
    self.name1 = name1
    self.coef = coef
    self.conc = conc
reactant = [Reactant("Reactant A",1,0.8),
            Reactant("Reactant B",2,2.15)]

#A class is defined for the products telling about the stoich
class Product :
  def __init__(self, name, coef, conc):
    self.name = name
    self.coef = coef
    self.conc = conc
product = [Product("Product 1",1,0), 
           Product("Product 2",2,0)]    



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


# In[93]:





# In[ ]:






#The volume of each inlet stream is the flow times the loading period. The total volume is the sum of the volumes 
#of all of the inlet streams.

#An empty array is defined to later contain the volume of each inletstream volume
V = [];
#A loop is made over each of the ilet streams to calculate the volume as flow times loading period.
for i in inletstreams:
    v = i.Fi*Tload
    #The value of each vinlet stream volume is assigned to the array V
    V.append(v)
#The total volume is the sum of the volumes of each inlet stream.     
Vtot = sum(V)


#beginning concentrations
#The concentration of each substance in the tank when it is filled will now be calculated as Ci0=Ci_inlet*Vi/Vtot 
#an empty array is defined to contain the concentration in each inlet stream
Ci0 = [];
for i in inletstreams:
    ci0 = i.Ci*i.Fi*Tload/Vtot
    Ci0.append(ci0)
    
#ending concentrations of reactants and products
#The concentrations in the ending of the reactants can be calculated in the conversion as Ci=Ci0*(1-X) and
#the concentration of the products can be calculated as Ci=Ci0*X

Ci_reactants = Ci0*(1-reaction.X)

