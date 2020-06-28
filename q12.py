import matplotlib as mpl
mpl.use('Qt5Agg')
import matplotlib.pyplot as plt
import numpy as np

###############
# Question 12a: Plot f(x) and g(x)
###############
x = np.arange(0.0, 3.01, 0.01)
p = 10.0
f = p * np.sin(x)
g = np.exp(x)

plt.plot(x, f, 'b')
plt.plot(x, g, 'g')
plt.xlabel('x')
plt.ylabel('f(x) and g(x)')
plt.title('f(x) = 10sin(x), g(x) = e^x')
axes = plt.gca()
axes.set_xlim([0,3])
axes.set_ylim([0,20])
plt.show()

###############
# Question 12b: Find the second intersection between f(x) and g(x)
###############
def fun(x, p):
    ''' Our function f(x) - g(x). '''
    return p * np.sin(x) - np.exp(x)


def findroots(p):
    ''' Find the roots for f(x) - g(x) with the given value for p. 
    
        This function uses the bisection method.
    '''
    # Initial values for the search domain [x1, x2]
    x1 = 1
    x2 = 3
    # Initial precision, take a large number
    prec = 1e3
    while prec > 1e-7:
        # Calculate x-coordinate of midpoint
        m = 0.5* (x2 + x1)

        # Calculate y-values for x1, m, and x2
        y1 = fun(x1, p)
        ym = fun(m, p)
        y2 = fun(x2, p)

        # Bisection method: if y1 and ym have the same sign, set x1 to m
        # otherwise, set x2 to m
        if y1 * ym > 0.0:
            x1 = m
        else:
            x2 = m
        # Update the precision
        prec = ym
    # Return the final x-coordinate of the root of f(x) - g(x)
    return m

###############
# Question 12c
###############

# Here we also use the bisection method
p1 = 5
p2 = 10

prec = 1e3
while prec > 1e-7:
    # Calculate midpoint
    pm = 0.5 * (p1 + p2)

    x1 = findroots(p1)
    xm = findroots(pm)
    x2 = findroots(p2)

    # Check using bisection method
    if (x1 - 2.0) * (xm - 2.0) > 0.0:
        p1 = pm
    else:
        p2 = pm
    # Update the precision
    prec = (xm - 2.0)

print(f'The intersection between f(x) and g(x) lies at x=2.0 for p = {pm}')
