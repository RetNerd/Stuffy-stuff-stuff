import numpy as np
from numpy import genfromtxt
from approxsq import approxsq
def geneticsq(pars):
	ret=0
	data = genfromtxt("data.csv", delimiter=';')#data = genfromtxt("values.csv", delimiter=',') CHANGED
	for idx, val in enumerate(data):
		ret=ret+np.abs(approxsq(idx, pars)-val)
	return ret
