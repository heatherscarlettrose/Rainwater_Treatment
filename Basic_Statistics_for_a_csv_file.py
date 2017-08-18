#Getting Basic Statistics for a .csv file

#Import Pandas, Matplotlib, Scipy Stats and Numpy (packages for Python, be sure you have them installed)
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

#Import your data by definining the data frame (be sure you are in the right directory)
data = pd.read_csv('My_Data.csv')

#View Columns of csv file
data.columns

#Chose a column you would like to inspect and define (be sure to use the column's exact name is shown above)
ColumnA = data['ColumnA']

#Extract Values from your column by defining a ColumnValues variabe
ColumnA_Values = ColumnA.values

#Take a look at your data by plotting a quick histogram
plt.hist(ColumnA_Values,bins=100) #What are bins???#

#Find the mean of your column
mean(ColumnA_Values)
#alternative
np.mean(ColumnA_Values)

#Find the median of your column
median(ColumnA_Values)
#alternative
np.median(ColumnA_Values)

#Find the mode of your column
stats.mode(ColumnA_Values)
#your mode is the number after mode=array([]) and the count=array([]) is the number of times this value appears

#Find the standard deviation of your column
np.std(ColumnA_Values)

#Want to do it all in one go? Create the function below, or import the Python file BasicStats.py

#This function gets basic statistics for a selected column

import numpy as np
from scipy import stats

def Get_Stats(Column):
    mean = np.mean(Column)
    print "mean", mean
    median = np.median(Column)
    print "median", median
    mode = stats.mode(Column)
    print "mode", mode
    min_value = np.min(Column)
    print "minimum value", min_value
    max_value = np.max(Column)
    print "maximum value", max_value
    std = np.std(Column)
    print "standard deviation", std     
    