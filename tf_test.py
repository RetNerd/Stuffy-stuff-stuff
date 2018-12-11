#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 23:46:26 2018

@author: rnerd
"""

import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model('network.hdf5')
print(' Test prediction:')
print(model.predict_proba(np.array([[1, 1, 0, 0]])))