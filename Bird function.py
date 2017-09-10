import math as m
import numpy as np
#Bird Function
#-------------------------------------------------------------
# Fitness Function parameters
#-------------------------------------------------------------
D       = 2    # Problem Dimension
LB      = -2*m.pi   # Set Size Lower Bound
UB      = 2*m.pi    # Set Size Upper Bound


#-------------------------------------------------------------
# Fitness Function
#-------------------------------------------------------------

def FitnessFunction(x):
    s = np.sin(x[0])*np.exp(1-np.cos(x[1]))**2 + np.cos(x[1])*np.exp(1-np.sin(x[0]))**2 + (x[0]-x[1])**2
    return s
