import math as m
import numpy as np
#Bartel Conn function
#-------------------------------------------------------------
# Fitness Function parameters
#-------------------------------------------------------------
D       = 2    # Problem Dimension
LB      = -500   # Set Size Lower Bound
UB      = 500    # Set Size Upper Bound


#-------------------------------------------------------------
# Fitness Function
#-------------------------------------------------------------
def FitnessFunction(x):
    s = abs(x[0]**2 + x[1]**2 + x[0]*x[1]) + abs(np.sin(x[0])) + abs(np.cos(x[1]))
    return s
