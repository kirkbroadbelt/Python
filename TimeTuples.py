# ST114: Homework 11
# Name: Kirk Broadbelt

# Instructions:
# In this assignment, we will write some functions using the
# data structures you've learned about to do some simple
# analysis of results from the 2019 Tobacco Road Marathon.
#
# A Python file homework11.py has been provided for you. You will need to
# edit it and push it to your ncsu repo:
# 'https://github.ncsu.edu/your-Unity-ID/you-Unity-IDST114/HW11/homework11.py'.

def text2list(input_file_name):
    """ (str) -> list

    Reads in a text file with one string per line and returns
    a list of strings.
    """
    with open(input_file_name) as input_file:
        lines = input_file.readlines()

    n = len(lines)
    x = list(range(n))
    for i in range(n):
        x[i] = lines[i].strip()
        
    return x
marathon = text2list('marathon.txt')

# Problem 1.

def list2tuples(L):
    """ (list) -> tuple

    Convert a list of strings of the form "hh:mm:ss.sss" into a list
    of tuples (hour, minute, second), where hour, minute, and second are
    floats.
    """
    tupleList = []
    for i in range(len(L)):
        hr = float(L[i][0:2])
        mins = float(L[i][3:5])
        sec = float(L[i][6:])
        tupleList.append((hr, mins, sec))
    return(tupleList)

times = list2tuples(marathon)
# Problem 2

def time_tuples2list_of_minutes(time_tuple):
    """ (list) -> list

    Convert a list of tuples of the form (hour, minute, second), where
    hour, minute, and second are floats into a list of minutes in floats.
    """
    minuteList = len(time_tuple) * [0]
    for i in range(len(time_tuple)):
        minuteList[i] = time_tuple[i][0] * 60
        minuteList[i] = minuteList[i] + time_tuple[i][1]
        minuteList[i] = minuteList[i] + time_tuple[i][2] / 60
    return(minuteList)
time_in_minutes = time_tuples2list_of_minutes(times)
# Problem 3

def list_of_minutes2time_tuples(minute_list):
    """ (list) -> list

    Convert a list of minutes in floats to a list of tuples of the form (hour, minute, second), where
    hour, minute, and second are floats.
    """
    tupleList = []
    for i in range(len(minute_list)):
        hr = minute_list[i] // 60
        mins = (minute_list[i] - 60 * hr) // 1
        sec = round(60 * (minute_list[i] - 60 * hr - mins), 1)
        tupleList.append((hr, mins, sec))
    return(tupleList)
times_tuples_again = list_of_minutes2time_tuples(time_in_minutes)
print( times == times_tuples_again)
#print(times_tuples_again)
# Problem 4
#print(list_of_minutes2time_tuples(time_tuples2list_of_minutes(list2tuples(text2list('marathon.txt')))))
def top_k_times(time_tuple, k):
    """ (list, int) -> list

    Returns the $k$ fastest times of tuples of the form (hour, minute, second).
    """
    pass
    list_of_top_times = []
    time_tuple.sort()
    for i in range(k):
        print('{}: {} hours, {} minutes, and {} seconds'.format(i+1,int(time_tuple[i][0]),int(time_tuple[i][1]),time_tuple[i][2]))
        list_of_top_times.append(time_tuple[i])
    #print(list_of_top_times)
    return list_of_top_times
top10 = top_k_times(times,10)

# Problem 5

def average_time(time_tuple):
    """ (list) -> tuple

    Take a list of tuples of the form (hour, minute, second), where
    hour, minute, and second are floats and return the average race time in
    the form of a tuple (hour, minute, second).
    """
    L = []
    times = time_tuples2list_of_minutes(time_tuple)
    avg = sum(times)/len(times)
    #print(avg)
    L.append(avg)
    final_avg = list_of_minutes2time_tuples(L)
    #print('The average time was {} hours, {} minutes, and {} seconds'.format(final_avg[0][0],final_avg[0][1],final_avg[0][2]))
    #print(final_avg[0])
    return final_avg[0]
average = average_time(times)
print('The average time was {} hours, {} minutes, and {} seconds'.format(average[0],average[1],average[2]))
#print(average)






    
