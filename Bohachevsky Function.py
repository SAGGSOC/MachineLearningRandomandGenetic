import math as m
import numpy as np
#Bohachevsky Function
#-------------------------------------------------------------
# Fitness Function parameters
#-------------------------------------------------------------
D       = 2    # Problem Dimension
LB      = -100   # Set Size Lower Bound
UB      = 100    # Set Size Upper Bound


#-------------------------------------------------------------
# Fitness Function
#-------------------------------------------------------------

def fitnessfunction(x):
    s = x[0]**2 + 2*x[1]**2-0.3*cos(3*m.pi.x[0])-0.4*cos(4*m.pi*x[1])+0.7
    return s
