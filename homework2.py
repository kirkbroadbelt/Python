# ST114: Homework 2
# Name:Kirk Broadbelt

# Instructions:
#   In this assignment, we will be computing quantities needed to perform
#   the classic t-test. There are many variations on the t-test, but they all
#   require computing a sample mean and sample standard deviation.
#
#   This Python file homework2.py has been provided for you. You will need to
#   edit it and push it to your ncsu repo:
#   'https://github.ncsu.edu/your-UnityID/you-UnityIDST114/HW2/homework2.py'.
#
#   Use the following 5 numbers: -1.21, 0.28, 1.08, -2.35, 0.43, 0.51.

x1 = -1.21
x2 = 0.28
x3 = 1.08
x4 = -2.35
x5 = 0.43
x6 = 0.51
n = 6

# Problem 1.
sample_mean = (x1 + x2 + x3 + x4 + x5 + x6) / 6
print(sample_mean)

# Problem 2.
sample_variance = (1 / (n-1)) * ( (pow (x1 - sample_mean , 2)) + (pow (x2 - sample_mean , 2)) + (pow (x3 - sample_mean , 2)) + (pow (x4 - sample_mean , 2)) + (pow (x5 - sample_mean , 2)) + (pow (x6 - sample_mean , 2)) )
print(sample_variance)

# Problem 3.
sample_standard_deviation = pow(sample_variance, 0.5)
print(sample_standard_deviation)

# Problem 4.
standard_error = sample_standard_deviation / pow(n, 0.5)
print(standard_error)

# Problem 5.
t_statistic = (sample_mean - 0 ) / standard_error
print(t_statistic)

# Problem 6.
t_statistic = (sample_mean - 0.5) / standard_error
print(t_statistic)
