import numpy as np
#import pandas as pd
from numpy import genfromtxt
from approxsq import approxsq

def geneticsq(pars):
	ret=0
	data = genfromtxt("values.csv", delimiter=',')

	for idx, val in enumerate(data):
		ret=ret+np.abs(approxsq(idx, pars)-val)

	return ret
