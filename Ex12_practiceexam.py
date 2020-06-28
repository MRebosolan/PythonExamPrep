from math import e
import numpy as np
import matplotlib.pyplot as plt

p = 10
x_array = np.linspace(0, 3, 1000)
y1_array = p * np.sin(x_array)
y2_array = e ** x_array
x_locations = []


def function(x, p):
    return p * np.sin(x) - np.exp(x)

def bisection(p):

    x1 = 1
    x2 = 3
    prec = 1e3

    while prec > 1e-7:
        m = 0.5 * (x1 + x2)
        y1 = function(x1, p)
        y2 = function(x2, p)
        ym = function(m, p)

        if y1 * ym > 0.0:
            x1 = m
        else:
            x2 = m
        prec = ym
    return m

print(bisection(10))

