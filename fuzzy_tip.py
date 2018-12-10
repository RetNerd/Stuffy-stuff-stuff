#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 18:48:01 2018

@author: rnerd
"""

import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl
from mpl_toolkits.mplot3d import Axes3D  # Required for 3D plotting

# New Antecedent/Consequent objects hold universe variables and membership
# functions
quality = ctrl.Antecedent(np.arange(6, 17, 0.1), 'quality') #quality = ctrl.Antecedent(np.arange(0, 10, 0.1), 'quality') CHANGED
service = ctrl.Antecedent(np.arange(8, 18, 0.1), 'service') #service = ctrl.Antecedent(np.arange(0, 10, 0.1), 'service') CHANGED
tip = ctrl.Consequent(np.arange(-5, 26, 0.1), 'tip')  #tip = ctrl.Consequent(np.arange(0, 25, 0.1), 'tip') CHANGED


quality['poor'] = fuzz.zmf(quality.universe, 6,17) #quality['poor'] = fuzz.zmf(quality.universe, 0,5) CHANGED
#quality['average'] = fuzz.gaussmf(quality.universe,5,1) CHANGED
quality['good'] = fuzz.smf(quality.universe,8,18) #quality['good'] = fuzz.smf(quality.universe,5,10) CHANGED

service['fast'] = fuzz.zmf(service.universe, 8,18) #service['poor'] = fuzz.zmf(service.universe, 0,5) CHANGED
#service['average'] = fuzz.gaussmf(service.universe,5,1) CHANGED
service['slow'] = fuzz.smf(service.universe,8,18) #service['good'] = fuzz.smf(service.universe,5,10) CHANGED

tip['low'] = fuzz.trimf(tip.universe, [-5, 3, 11])  #tip['low'] = fuzz.trimf(tip.universe, [0, 0, 13]) CHANGED
tip['medium'] = fuzz.trimf(tip.universe, [3, 11, 19]) #tip['medium'] = fuzz.trimf(tip.universe, [0, 13, 25]) CHANGED
tip['high'] = fuzz.trimf(tip.universe, [11, 19, 26]) #tip['high'] = fuzz.trimf(tip.universe, [13, 25, 25]) CHANGED

"""
To help understand what the membership looks like, use the ``view`` methods.
"""

# You can see how these look with .view()
#plt.ion()
#quality['average'].view()
#plt.title('Quality')
#plt.ioff()
"""
.. image:: PLOT2RST.current_figure
"""
#plt.ion()
#service.view()
#plt.title('Service')
#plt.ioff()
"""
.. image:: PLOT2RST.current_figure
"""
#plt.ion()
#tip.view()
#plt.title('Tip')
#plt.ioff()
"""
.. image:: PLOT2RST.current_figure


Fuzzy rules
-----------

Now, to make these triangles useful, we define the *fuzzy relationship*
between input and output variables. For the purposes of our example, consider
three simple rules:

1. If the food is poor OR the service is poor, then the tip will be low
2. If the service is average, then the tip will be medium
3. If the food is good OR the service is good, then the tip will be high.

Most people would agree on these rules, but the rules are fuzzy. Mapping the
imprecise rules into a defined, actionable tip is a challenge. This is the
kind of task at which fuzzy logic excels.
"""

rule1 = ctrl.Rule(quality['poor'] & service['fast'], tip['medium']) #rule1 = ctrl.Rule(quality['poor'] | service['poor'], tip['low']) CHANGED
rule2 = ctrl.Rule(quality['poor'] & service['slow'], tip['low'])#rule2 = ctrl.Rule(service['average'], tip['medium']) CHANGED
rule3 = ctrl.Rule(quality['good'] & service['fast'], tip['high'])#rule3 = ctrl.Rule(service['good'] | quality['good'], tip['high']) CHANGED
rule4 = ctrl.Rule(quality['good'] & service['slow'], tip['medium']) #NEW

"""
.. image:: PLOT2RST.current_figure

Control System Creation and Simulation
---------------------------------------

Now that we have our rules defined, we can simply create a control system
via:
"""

tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4]) #tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3]) CHANGED

"""
In order to simulate this control system, we will create a
``ControlSystemSimulation``.  Think of this object representing our controller
applied to a specific set of cirucmstances.  For tipping, this might be tipping
Sharon at the local brew-pub.  We would create another
``ControlSystemSimulation`` when we're trying to apply our ``tipping_ctrl``
for Travis at the cafe because the inputs would be different.
"""

tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

"""
We can now simulate our control system by simply specifying the inputs
and calling the ``compute`` method.  Suppose we rated the quality 6.5 out of 10
and the service 9.8 of 10.
"""
# Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
# Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
tipping.input['quality'] = 6.5
tipping.input['service'] = 9.8

# Crunch the numbers
tipping.compute()

"""
Once computed, we can view the result as well as visualize it.
"""
#plt.ion()
print(tipping.output['tip'])
#tip.view(sim=tipping)
#plt.title('Result')
#plt.show()
#plt.ioff()

"""
.. image:: PLOT2RST.current_figure

The resulting suggested tip is **20.24%**.

Final thoughts
--------------

The power of fuzzy systems is allowing complicated, intuitive behavior based
on a sparse system of rules with minimal overhead. Note our membership
function universes were coarse, only defined at the integers, but
``fuzz.interp_membership`` allowed the effective resolution to increase on
demand. This system can respond to arbitrarily small changes in inputs,
and the processing burden is minimal.

"""

# We can simulate at higher resolution with full accuracy
upsampled = np.linspace(0, 10, 10)
x, y = np.meshgrid(upsampled, upsampled)
z = np.zeros_like(x)

# Loop through the system 10*10 times to collect the control surface
for i in range(10):
    for j in range(10):
        tipping.input['quality'] = x[i, j]
        tipping.input['service'] = y[i, j]
        tipping.compute()
        z[i, j] = tipping.output['tip']

# Plot the result in pretty 3D with alpha blending
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='viridis',
                       linewidth=0.4, antialiased=True)

cset = ax.contourf(x, y, z, zdir='z', offset=-2.5, cmap='viridis', alpha=0.5)
cset = ax.contourf(x, y, z, zdir='x', offset=13, cmap='viridis', alpha=0.5)
cset = ax.contourf(x, y, z, zdir='y', offset=13, cmap='viridis', alpha=0.5)

ax.view_init(30, 200)
plt.show()
plt.ioff()