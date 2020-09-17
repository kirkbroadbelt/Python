## Collaborators: Emily Oppold, Morgan Kuchenbrod
## Please list all sources, including those outside of class like StackExchange.

from data import Data
from linear_regression import SLR
import csv

def read_data(input_file_name):
    """ (str) -> list, list

    Read data from the path specified by the string input_file.
    Data looks like:

    18,  120
    20,  110
    22,  120
    25,  135

    Output two lists, one for each column of data.
    """
    try:
        x = []
        y = []     
        with open(input_file_name, 'r') as csvfile:
            data_reader = csv.reader(csvfile, delimiter = ',')

            for row in data_reader:
                x.append(float(row[0].strip()))
                y.append(float(row[1].strip()))
        
    except FileNotFoundError:
        x, y = None, None
        print("Unable to open and read {0}".format(input_file_name))
        
    finally:
        return (x, y)
     
    
filename = 'bmi_vs_sbp.csv'
x, y = read_data(filename)
dat = Data(x,y)
lm = SLR(dat)
print(lm)
lm.plot()