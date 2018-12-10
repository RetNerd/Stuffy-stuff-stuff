import numpy as np
#import pandas as pd

base=np.arange(-5.0, 5.0, 0.1)
noise=np.random.rand(len(base))+10
ret=np.power(base, 2)+noise

np.savetxt("values.csv", ret, delimiter=",")

#df = pd.DataFrame(ret)
#df.to_csv("values.csv")
