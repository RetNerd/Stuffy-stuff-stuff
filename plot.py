#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 18:42:50 2018

@author: rnerd
"""

import matplotlib.pyplot as plt
import numpy as np
data = np.genfromtxt(fname = 'data.csv', delimiter = ';')
plt.plot(data)
plt.show()