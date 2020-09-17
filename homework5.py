# ST114: Homework 5
# Name: Kirk Broadbelt

# Instructions:
#  In this assignment, we will practice using the list type.
#
# A Python file homework5.py has been provided for you. You will need to
# edit it and push it to your ncsu repo:
# 'https://github.ncsu.edu/your-Unity-ID/you-Unity-IDST114/HW5/homework5.py'.
from math import inf
# Problem 1.
def sample_mean(x):
    """(list) -> float
    Returns the sample mean of the input variables

    >>> sample_mean([1,2,3,4])
    2.5
    >>> sample_mean([5,12,52,2])
    17.75
    """
    return sum(x) / len(x)
    
# Problem 2.
def sample_variance(x):
    """(list) -> float
    Returns the sample variance of the input variables
    
    >>> sample_variance([1,2,3,4])
    1.6666666666666665
    
    >>> sample_variance([5,12,52,2])
    538.9166666666666
    """
    mean = sample_mean(x)
    summation = 0
    for i in range(len(x)):
        summation += pow(x[i] - mean, 2)
    return summation * (1 / (len(x) - 1) )

# Problem 3.
def sample_standard_deviation(x):
    """(list) -> float
    Returns the sample standard deviation of the input variables

    >>> sample_standard_deviation([1,2,3,4])
    1.2909944487358056

    >>> sample_standard_deviation([5,12,52,2])
    23.214578752729214
    """
    return pow( sample_variance(x), .5)

# Problem 4.
def standard_error(x):
    """(list) -> float
    Returns the standard error of the input variables
    
    >>> standard_error([1,2,3,4])
    0.6454972243679028
    
    >>> standard_error([5,12,52,2])
    11.607289376364607
    """
    return sample_standard_deviation(x) / pow(len(x) , 0.5)

# Problem 5.
def t_statistic(x, mu):
    """(list) -> float
    Returns the test statistic of the input variables
    
    >>> t_statistic([1,2,3,4],.5)
    3.0983866769659336
    
    >>> t_statistic([5,12,52,2],1)
    1.4430587070662044
    """
    if standard_error(x) == 0:
        return inf
    else:
        return(sample_mean(x) - mu) / standard_error(x)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
#print(t_statistic([1,1,1],1))
