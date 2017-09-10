import math as m
import numpy as np
#Brent Function
#-------------------------------------------------------------
# Fitness Function parameters
#-------------------------------------------------------------
D       = 3    # Problem Dimension
LB      = -10   # Set Size Lower Bound
UB      = 10    # Set Size Upper Bound


#-------------------------------------------------------------
# Fitness Function
#-------------------------------------------------------------

def FitnessFunction(x):
    s = (x[0]+10)**2 + (x[1]+10)**2 + np.exp(-x[0]**2-x[1]**2)
    return s
