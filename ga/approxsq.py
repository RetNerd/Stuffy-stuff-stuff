import numpy as np
def approxsq(i, pars):
	return (np.sin((i+pars[2])/pars[1])+pars[0])
