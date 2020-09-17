# ST114: Homework 3
# Name: Kirk Broadbelt

# Instructions:
#   In this assignment, we will write functions to compute quantities needed to perform
#   the classic t-test. There are many variations on the t-test, but they all
#   require computing a sample mean and sample standard deviation.
#
#   This Python file homework3.py has been provided for you. You will need to
#   edit it and push it to your ncsu repo:
#   ‘https://github.ncsu.edu/your-Unity-ID/you-Unity-IDST114/HW3/homework3.py’
#



# Problem 1.
def sample_mean(x1,x2,x3,x4):
    """(number,number,number,number) -> float
    Returns the sample mean of the input variables

    >>> sample_mean(1,2,3,4)
    2.5
    >>> sample_mean(5,12,52,2)
    17.75
    """
    return (x1 + x2 + x3 + x4) / 4

print(sample_mean(1,2,3,4))
print(sample_mean(5,12,52,2))

# Problem 2.
def sample_variance (x1,x2,x3,x4):
    """(number,number,number,number) -> float
    Returns the sample variance of the input variables
    
    >>> sample_variance(1,2,3,4)
    1.6666666666666665
    
    >>> sample_variance(5,12,52,2)
    538.9166666666666
    """
    mean = sample_mean(x1,x2,x3,x4)
    return (1 / (4-1)) * ( (pow (x1 - mean , 2) ) + (pow (x2 - mean , 2)) + (pow (x3 - mean , 2)) + (pow (x4 - mean , 2) ) )
                           
print(sample_variance(1,2,3,4))
print(sample_variance(5,12,52,2))

# Problem 3.
def sample_standard_deviation(x1,x2,x3,x4):
    """(number,number,number,number) -> float
    Returns the sample standard deviation of the input variables

    >>> sample_standard_deviation(1,2,3,4)
    1.2909944487358056

    >>> sample_standard_deviation(5,12,52,2)
    23.214578752729214
    """
    return pow( sample_variance(x1,x2,x3,x4) , 0.5 )

print(sample_standard_deviation(1,2,3,4) )
print(sample_standard_deviation(5,12,52,2) )

# Problem 4.
def standard_error(x1,x2,x3,x4):
    """(number,number,number,number) -> float
    Returns the standard error of the input variables
    
    >>> standard_error(1,2,3,4)
    0.6454972243679028
    
    >>> standard_error(5,12,52,2)
    11.607289376364607
    """
    return sample_standard_deviation(x1,x2,x3,x4) / pow(4, 0.5)

print(standard_error(1,2,3,4) )
print(standard_error(5,12,52,2) )

# Problem 5.
def t_statistic(x1,x2,x3,x4,mu):
    """(number,number,number,number,number) -> float
    Returns the test statistic of the input variables
    
    >>> t_statistic(1,2,3,4,.5)
    3.0983866769659336
    
    >>> t_statistic(5,12,52,2,1)
    1.4430587070662044
    """
    return (sample_mean(x1,x2,x3,x4) - mu)  / standard_error(x1,x2,x3,x4)
print(t_statistic(1,2,3,4, 0.5) )
print(t_statistic(5,12,52,2, 1) )

import doctest
doctest.testmod()






