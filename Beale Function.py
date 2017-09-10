import math as m
import numpy as np
#Beale function
#-------------------------------------------------------------
# Fitness Function parameters
#-------------------------------------------------------------
D       = 2    # Problem Dimension
LB      = -4.5   # Set Size Lower Bound
UB      = 4.5    # Set Size Upper Bound


#-------------------------------------------------------------
# Fitness Function
#-------------------------------------------------------------

def FitnessFunction(x):
    s = (1.5 - x[0] + x[0]*x[1])**2 + (2.25-x[0] + x[0]*x[1]**2)**2 + (2.625 - x[0] + x[0]*x[1]**3)**2
    return s
