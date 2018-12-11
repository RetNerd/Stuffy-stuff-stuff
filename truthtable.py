#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 00:10:30 2018

@author: rnerd
"""
import numpy as np

def truth(truth):
	if truth:
		return 1
	else:
		return 0

def truthtable():
    A = [True, False]
    B = [True, False]
    C = [True, False]
    D = [True, False]
    Y = np.empty(1, dtype = int)
    X = np.empty(4, dtype = int)
    for a in A:
        for b in B:
            for c in C:
                for d in D:
                    formula = not (a and b) or (c or d) #modify this to your own 4 variable logical function
                    Y = np.vstack((Y , truth(formula)))
                    X = np.vstack((X, [truth(a), truth(b), truth(c), truth(d)]))
    return [X[1:], Y[1:]]
print(truthtable())