# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ckjuBALovS5ztpxiWIurMPGHaMaNwhHK
"""

from sympy import*
from sympy import integrate

x=Symbol('x')

f = x*cos(x)
integrate(f,x)

f = ln(x)/x**2
integrate(f,x)

f = exp(x)
integrate(f,x)

f = x*exp(6*x)
integrate(f,x)

f = (3*x+5)*cos(x/4)
integrate(f,x)

f = x*sqrt(x+1)
integrate(f,x)