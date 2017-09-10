import math as m
import numpy as np
#Branin RCOS Function
#-------------------------------------------------------------
# Fitness Function parameters
#-------------------------------------------------------------
D       = 2    # Problem Dimension
LB      = -5   # Set Size Lower Bound
UB      = 15    # Set Size Upper Bound


#-------------------------------------------------------------
# Fitness Function
#-------------------------------------------------------------

def FitnessFunction(x):
    return (x[1] - (5.1*x[0]**2)/(4*np.pi**2) + 5*x[0]/np.pi - 6)**2 + 10*(1-1/(8*np.pi))*np.cos(x[0]) + 10
