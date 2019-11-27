#!/usr/bin/env python
# coding: utf-8

# In[77]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.integrate import fixed_quad
from scipy import integrate
from scipy.integrate import quad
from scipy.integrate import odeint
from sympy.solvers import solve
from sympy import Symbol
import math
from math import exp, expm1
from dataclasses import dataclass
from scipy.integrate import simps
from ipykernel import kernelapp
from scipy.integrate import dblquad
import numpy as np

names = ["A", "B"]
coefficients  = [1,-2]
initial_concentrations = [0.07174, 0]
orders = [1, 2]
kf = 0.5
kr = 0.5/0.1
Reversible = True

class reaction: 
    def __init__(self, names, coefficients, initial_concentrations, orders, kf, kr, Reversible = True):
        self.names = names
        self.coefficients = coefficients
        self.initial_concentrations = initial_concentrations
        self.orders = orders
        self.Reversible = Reversible
        self.kf = kf
        self.kr = 0
        self.t_end = 100
        self.t_start = 0
        self.steps = (self.t_end - self.t_start)*24
    def reactionfunc (self, C, t):
        
        coef_reactants = list(filter(lambda coefficients: coefficients >0, coefficients))
        coef_products = list(filter(lambda coefficients: coefficients <0, coefficients))
        
        n = len(coef_reactants)
        r = np.ones((n,1))
        if self.Reversible == True:
            self.kr = kr 
            self.ke = self.kf/self.kr
            forwardrate = 1
            reverserate = 1
            n = len(coefficients)
            r = np.zeros((n,1))
            for i in range(0,len(coef_reactants)):
                forward = C[i]**orders[i]
                forwardrate = forwardrate * forward 
            for i in range (len(coef_reactants),len(coefficients)):
                reverse = (orders[0]/orders[i]*C[i])**orders[i]
                reverserate = reverserate * reverse 
            rate = self.kf*(forwardrate - reverserate/self.ke)
            r[0,0] = rate
            dcdt = [];
            for i in range(0,len(coefficients)):
                r[i,0] = r[0]/self.coefficients[i]
                dcdt.append(-r[i,0])
    
            
        if self.Reversible == False: 
          
            rate1=1
            n = len(coefficients)
            r = np.zeros((n,1))
            
            for i in range(len(coef_reactants)):
                rates = C[i]**orders[i]
                rate1 = rate1 * rates
            rate = self.kf*rate1
            r[0] = rate
            dcdt = [];
            for i in range(len(coefficients)):
                r[i] = r[0]/self.coefficients[i]
                dcdt.append(-r[i])
            
        return (dcdt)   
    
    def solve(self):
        t = np.linspace(self.t_start,self.t_end,200)
        C = odeint(self.reactionfunc, self.initial_concentrations, t)
        fig = plt.figure()
        ax = plt.subplot(111)
        ax.plot(t,C, label = 'Ca')
        plt.title('Concentration profile of reactants and products')
        ax.legend()
        plt.show()
        return t,C
        
    
    

        
reaction = reaction(names, coefficients, initial_concentrations, orders, kf, kr, Reversible = True)


reaction.solve()


# In[10]:


np.zeros((4,1))


# In[62]:


0.07174*(1-1)


# In[78]:


0.07174*2


# In[ ]:




