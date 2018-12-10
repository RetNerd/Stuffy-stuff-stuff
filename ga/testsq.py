import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt
from approxsq import approxsq

def testsq(pars):

data = genfromtxt("data.csv", delimiter=';')	#data = genfromtxt("data.csv", delimiter=',') CHANGED
	ret=np.zeros(len(data))

	for idx, val in enumerate(data):
		ret[idx]=approxsq(idx, pars)

	plt.plot(data)
	plt.plot(ret)
	plt.show()

