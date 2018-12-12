#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 22:06:30 2018

@author: rnerd
"""
import numpy as np
#Takes 3 input, X and y are the logical functions input and output, N the number of examples generated from each row of the truthtable
def generatedata(X, y, N):
	outX = np.empty(4, dtype = int)
	outY = np.empty(1, dtype = int)
	for i, x in enumerate(X):
		outX=np.vstack((outX, x))
		outY=np.vstack((outY, y[i]))
		for j in np.arange(0, N):
			item = np.array(np.add(x, np.random.uniform(-0.05, 0.05, 4)))
			outX=np.vstack((outX, item))
			outY=np.vstack((outY, y[i]))
	return [outX, outY]
