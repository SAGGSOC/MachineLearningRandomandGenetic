import math as m
import numpy as np
#Box-Betts Quadratic Sum Function
#-------------------------------------------------------------
# Fitness Function parameters
#-------------------------------------------------------------
D       = 3    # Problem Dimension
LB      = 0.9   # Set Size Lower Bound
UB      = 11.2    # Set Size Upper Bound


#-------------------------------------------------------------
# Fitness Function
#-------------------------------------------------------------

def FitnessFunction(x):
	result = 0
	for i in range(D):
            s = m.exp(-0.1*(i+1)*x[0])-m.exp(-0.1*(i+1)*x[1])-m.exp(((-0.1*(i+1))-m.exp(-1*(i+1)))*x[2])
            result = result + g**2
        return round(result,2)    
