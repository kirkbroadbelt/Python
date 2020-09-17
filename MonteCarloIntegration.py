# ST114: Homework 6
# Name:Kirk Broadbelt

# Instructions:
#  In this assignment, we will practice using conditional statements and
#  importing from a module.
#
# A Python file homework6.py has been provided for you. You will need to
# edit it and push it to your ncsu repo:
# 'https://github.ncsu.edu/your-Unity-ID/you-Unity-IDST114/HW6/homework6.py'.

# Problem 1.
from math import tau, exp
import random
def gaussian(x):
    """(number) -> float
    Returns the Guassian density evaluated at x

    >>> gaussian(4)
    0.00013383022576488537
    >>> gaussian(2)
    0.05399096651318806
    """
    return pow(tau, -0.5) * exp( - pow(x,2)/ 2 )
print(gaussian(4))
print(gaussian(2))
# Problem 2.


def under_curve(x, y):
    """(number,number) -> Boolean
    Returns true if the coordinate pair (x,y) are are under the curve, false if not

    >>> under_curve(0,.1)
    True
    >>> under_curve(1,2)
    False
    """
    return 0 <= y and y <= gaussian(x)
print(under_curve(0,.1))
print(under_curve(1,2))
# Problem 3.

def greater_than(x, a):
    """(number,number) -> Boolean
    Returns true if x is greater than a, false if not

    >>> greater_than(1,2)
    False
    
    >>> greater_than(2,1)
    True
    """
    return x > a
print(greater_than(1,2))
print(greater_than(2,1))
# Problem 4.

def less_than(x, b):
    """(number,number) -> Boolean
    Returns true if x is less than b, and false if not

    >>> less_than(1,2)
    True

    >>> less_than(2,1)
    False
    """
    return x < b
print(less_than(1,2))
print(less_than(2,1))

# Problem 5.

def monte_carlo_gaussian(a, b, n):
    """(number,number,int) -> float
    Returns an estimate of the area under the Gaussian density curve over the interval (a,b)
    """
    counter = 0
    for i in range(n):
        x = random.uniform(a,b)
        y = random.uniform(0,gaussian(0))
        if under_curve(x,y) and greater_than(x,a) and less_than(x,b):
            counter += 1
    return counter / n * (b-a) * (gaussian(0))
           
        

# Problem 6. Print out estimates for different numbers of darts thrown.
print(monte_carlo_gaussian(-1.644854, 1.644854, 10) )
print(monte_carlo_gaussian(-1.644854, 1.644854, 100) )
print(monte_carlo_gaussian(-1.644854, 1.644854, 1000))
print(monte_carlo_gaussian(-1.644854, 1.644854, 10000))
print(monte_carlo_gaussian(-1.644854, 1.644854, 100000))
if __name__ == "__main__":
    import doctest
    doctest.testmod()
