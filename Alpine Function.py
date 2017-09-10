import math as m
import numpy as np
#Alpine Function
#-------------------------------------------------------------
# Fitness Function parameters
#-------------------------------------------------------------
D       = 10    # Problem Dimension
LB      = -10   # Set Size Lower Bound
UB      = 10    # Set Size Upper Bound


#-------------------------------------------------------------
# Fitness Function
#-------------------------------------------------------------

def FitnessFunction(x):
    s = sum(map(lambda nb: abs(nb*np.sin(nb) + 0.1*nb), x))
    return round(s,2)
