import math as np
#Ackley's Function
#-------------------------------------------------------------
# Fitness Function parameters
#-------------------------------------------------------------
D       = 10    # Problem Dimension
LB      = -35   # Set Size Lower Bound
UB      = 35    # Set Size Upper Bound


#-------------------------------------------------------------
# Fitness Function
#-------------------------------------------------------------

def FitnessFunction(x):
    part1 = -1.0 * 20 * np.exp(-1. * 0.02 * np.sqrt((1. / D) * sum(map(lambda nb: nb ** 2, x))))

    part2 = -1. * np.exp((1.0 / D) * \ sum(map(lambda nb: np.cos(2*np.pi * nb),x)))
    s = part1 + part2 + 20 + np.exp(1)
    return round(s,2)












