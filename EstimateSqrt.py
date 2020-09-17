# ST114: Homework 7
# Name: Kirk Broadbelt

# Instructions:
#  In this assignment, we will practice writing control flow for loops.
#
# A Python file homework7.py has been provided for you. You will need to
# edit it and push it to your ncsu repo:
# 'https://github.ncsu.edu/your-Unity-ID/you-Unity-IDST114/HW7/homework7.py'.

# Problem 1.

def square_root_for(a, x0, max_iter = 10, tol=1e-14):
    """ (number, integer, number) -> float

    Return an estimate of the square root of a number using the Heron's method.
        
    >>> square_root_for(5, 5)
    Iteration | Estimate         | Relative Change
    -------------------------------------------------
    1         | 3.00000000000000 | 0.4000000000000000
    2         | 2.33333333333333 | 0.2222222222222222
    3         | 2.23809523809524 | 0.0408163265306123
    4         | 2.23606889564336 | 0.0009053870529653
    5         | 2.23606797749998 | 0.0000004106060359
    6         | 2.23606797749979 | 0.0000000000000842
    7         | 2.23606797749979 | 0.0000000000000000
    2.23606797749979
    """
    change = 1
    print('Iteration | Estimate         | Relative Change')
    print('-------------------------------------------------')
    for i in range(1, max_iter):
        x_next = 0.5 * (x0 + a / x0)
        change = abs(x_next - x0) / x0
        print(f"{i}         | {x_next:.14f} | {change:.16f}")
        x0 = x_next
        if change < tol:
            break
    return x_next

           
# Don't change or delete the 5 lines of code below.
a = 5
max_iter = 100
tol = 1e-15
x_final = square_root_for(a, a, max_iter, tol)
print('Final estimate using square_root_for is {0}'.format(x_final))

# Problem 2.

def square_root_while(a, x0, tol=1e-14):
    """ (number, number, number) -> float

    Return an estimate of the square root of a number using the Heron's method.
        
    >>> square_root_while(5, 5)
    Iteration | Estimate         | Relative Change
    -------------------------------------------------
    1         | 3.00000000000000 | 0.4000000000000000
    2         | 2.33333333333333 | 0.2222222222222222
    3         | 2.23809523809524 | 0.0408163265306123
    4         | 2.23606889564336 | 0.0009053870529653
    5         | 2.23606797749998 | 0.0000004106060359
    6         | 2.23606797749979 | 0.0000000000000842
    7         | 2.23606797749979 | 0.0000000000000000
    2.23606797749979
    """
    change = 1
    i = 1
    print('Iteration | Estimate         | Relative Change')
    print('-------------------------------------------------')
    while change >= tol:
        x_next = 0.5 * ( x0 + a / x0)
        change = abs(x_next - x0) / x0
        print(f"{i}         | {x_next:.14f} | {change:.16f}")
        x0 = x_next
        i += 1
    return x_next
# Don't change or delete the 4 lines of code below.
a = 5
tol = 1e-15
x_final = square_root_while(a, a, tol)
print('Final estimate using square_root_while is {0}'.format(x_final))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
