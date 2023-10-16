# -*- coding: utf-8 -*-
"""Computes windchill as a function of
wind(mph)and temp (Fahrenheit)."""
Temp = input('Enter temp (Fahrenheit):')
Wind = input('Enter wind speed (mph):')
# Model Parameters
A=35.74;B=.6215;C=-35.74;D=.4275;e=.16
# Compute and display the windchill
WC = (A+B*float(Temp))+(C+D*float(Temp))*Wind**e
print(" Windchill: "+ str(round(WC)).center(4))

