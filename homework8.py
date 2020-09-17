# ST114: Homework 8
# Name: Kirk Broadbelt

# Instructions:
# In this assignment, we will practice using sorting and list comprehensions.
#
# A Python file homework8.py has been provided for you. You will need to
# edit it and push it to your ncsu repo:
# 'https://github.ncsu.edu/your-Unity-ID/you-Unity-IDST114/HW8/homework8.py'.
import math
# Problem 1.
def my_median(x):
    """ (list) -> number
    Returns the median of a list of numbers
    
    >>> my_median([9,2,7,5,3])
    5
    >>> my_median([1,2,3,4])
    2.5
    """
    x.sort()
    y = x
    n = len(x)
    if n % 2 == 1:
        return y[(n + 1)// 2 - 1]
    elif n % 2 == 0:
        return (y[n // 2 - 1] + y[n // 2] ) / 2
#print(my_median([9,2,7,5,3]) )
#print(my_median([1,2,3,4]))
    
# Problem 2
def mad_for(x):
    """ (list) -> number
    Returns the MAD of a list
    
    >>> mad_for([1,2,3,4,5])
    1
    >>> mad_for([1,2,3,4])
    1.0
    """
    d = [0]*len(x)
    medianx = my_median(x) 
    for i in range(len(x)):
        d[i] = abs(x[i] - medianx)
    return my_median(d)
#print(mad_for([1,2,3,4,5]))

# Problem 3
def mad_lc(x):
    """ (list) -> number
    Returns the MAD of a list
    
    >>> mad_lc([1,2,3,4,5])
    1
    >>> mad_lc([1,2,3,4])
    1.0
    """
    d = [0] * len(x)
    medianx = my_median(x)
    d = [abs(x[i]-medianx) for i in range(len(x))]
    return my_median(d)
#print(mad_lc([1,2,3,4,5]))

# Problem 4
def log_transform(x):
    """ (list) -> list
    It returns a list y containing the log-transformed values of x

    >>> log_transform([1,2])
    [0.0, 0.6931471805599453]
    >>> log_transform([1,2,-1,0])
    [0.0, 0.6931471805599453, nan, nan]
    """
    y = [math.log(x[i]) if x[i] > 0 else math.nan for i in range(len(x)) ]
    return y
#print(log_transform([1,2]))
#print(log_transform([1,2,-1,0]))

# Problem 5
def apply_for(x, f):
    """(list,function) -> list
    Returns a list obtained by applying f to each list of numbers in x
    >>> apply_for([[1,2,3,4,5],[1,2],[1,5,7]],my_median)
    [3, 1.5, 5]
    >>> apply_for([[1,2,3,4,5],[1,2],[1,5,7]],mad_for)
    [1, 0.5, 2]
    >>> apply_for([[1,2,3,4,5],[1,2],[1,5,7]],mad_lc)
    [1, 0.5, 2]
    >>> apply_for([[1,2,3,4,5],[1,2],[1,5,7]],log_transform)
    [[0.0, 0.6931471805599453, 1.0986122886681098, 1.3862943611198906, 1.6094379124341003], [0.0, 0.6931471805599453], [0.0, 1.6094379124341003, 1.9459101490553132]]
    >>> apply_for([[-1,2],[-1,-5,7]],log_transform)
    [[nan, 0.6931471805599453], [nan, nan, 1.9459101490553132]]
    """
    y = x[:]
    for i in range(len(x)):
        y[i] = f(x[i])
    return y
#print(apply_for([[1,2,3,4,5],[1,2],[1,5,7]],my_median))
#print(apply_for([[1,2,3,4,5],[1,2],[1,5,7]],mad_for))
#print(apply_for([[1,2,3,4,5],[1,2],[1,5,7]],mad_lc))
#print(apply_for([[1,2,3,4,5],[1,2],[1,5,7]],log_transform))

# Problem 6
def apply_lc(x, f):
    """(list,function) -> list
    Returns a list obtained by applying f to each list of numbers in x
    >>> apply_lc([[1,2,3,4,5],[1,2],[1,5,7]],my_median)
    [3, 1.5, 5]
    >>> apply_lc([[1,2,3,4,5],[1,2],[1,5,7]],mad_for)
    [1, 0.5, 2]
    >>> apply_lc([[1,2,3,4,5],[1,2],[1,5,7]],mad_lc)
    [1, 0.5, 2]
    >>> apply_lc([[1,2,3,4,5],[1,2],[1,5,7]],log_transform)
    [[0.0, 0.6931471805599453, 1.0986122886681098, 1.3862943611198906, 1.6094379124341003], [0.0, 0.6931471805599453], [0.0, 1.6094379124341003, 1.9459101490553132]]
    >>> apply_lc([[-1,2],[-1,-5,7]],log_transform)
    [[nan, 0.6931471805599453], [nan, nan, 1.9459101490553132]]
    """
    y = x[:]
    y = [f(x[i]) for i in range(len(x))]
    return y
#print(apply_lc([[1,2,3,4,5],[1,2],[1,5,7]],my_median))
#print(apply_lc([[1,2,3,4,5],[1,2],[1,5,7]],mad_for))
#print(apply_lc([[1,2,3,4,5],[1,2],[1,5,7]],mad_lc))
#print(apply_lc([[1,2,3,4,5],[1,2],[1,5,7]],log_transform))

if __name__ == "__main__":
    import doctest
    doctest.testmod()

  
