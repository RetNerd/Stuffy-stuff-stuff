#from keras.models import Sequential
#from keras.layers.core import Dense, Dropout, Activation
#from keras.optimizers import SGD
import tensorflow as tf
import numpy as np
from randomdatagenerator import generatedata
# Define the input and the expected output
X = np.array([[0,0,0,0],[0,0,0,1],[0,0,1,0],[0,0,1,1],
			  [0,1,0,0],[0,1,0,1],[0,1,1,0],[0,1,1,1],
			  [1,0,0,0],[1,0,0,1],[1,0,1,0],[1,0,1,1],
			  [1,1,0,0],[1,1,0,1],[1,1,1,0],[1,1,1,1]])
y = np.array([[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[0],[1],[1],[1]])
# The Sequential model is a linear stack of layers.
IN, OUT = generatedata(X,y, 100)
model = tf.keras.models.Sequential()
# The model needs to know what input shape it should expect. For this reason, the first layer in a  Sequential model (and only the first, because following layers can do automatic shape inference) needs to receive information about its input shape.
# Some 2D layers, such as Dense, support the specification of their input shape via the argument input_dim
model.add(tf.keras.layers.Dense(4 ,input_shape = (4, ) , activation=tf.nn.relu))
#model.add(tf.keras.layers.Dense(5, activation = tf.nn.sigmoid))
model.add(tf.keras.layers.Dense(1, activation = tf.nn.sigmoid))

# Before training a model, you need to configure the learning process, which is done via the compile method
# It receives three arguments:
# - An optimizer (e.g. SGD - Stochastic gradient descent optimizer)
# - A loss function
# For a binary classification problem: binary_crossentropy
# For a mean squared error regression problem: mse
# For a multi-class classification problem: categorical_crossentropy
# - A list of metrics
# For any classification problem you will want to set this to metrics=['accuracy'].
model.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
# Keras models are trained on Numpy arrays of input data and labels. For training a model, you will typically use the fit function.
model.fit(IN, OUT, batch_size=4, epochs=500)
model.save('network.hdf5')
print('Rounded prediction:')
print(np.round(model.predict_proba(X),2))
"""
[[0.01]
 [1.  ]
 [1.  ]
 [0.01]]
"""