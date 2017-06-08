# -*- coding: utf-8 -*-
#Description: Filter out rows with text criteria in a csv file using Pandas in Python.
#Save a new csv file excluding deleted rows.
#Be sure your csv file is in your present working directory (pwd).

#Note: I made sure the text criteria for deleting was only present in one column.
#For example, “leak” was a type of category listed under my “CountAs” column.
#This code deleted all rows in the “CountAs” column that contained the word “leak”.
#Also keep in mind that Python is case sensitive for text criteria (and in general).

#This code uses the python package pandas, which is used for data analysis. 

import pandas as pd

#Define data and load your csv file:
data = pd.read_csv('full/directory/My_File.csv')

#Filter rows based on text criteria:
filtered_data = data[data.MyColumn != 'text criteria']

#Save new filtered csv file:
filtered_data.to_csv('My_New_file.csv')

#Be sure to give your new file a different name to prevent overwriting your original data!

#Open your new filtered csv and see the unwanted rows have been deleted!

#Note: You can also filter rows based on criteria, such as a numerical value range.
#I found this Youtube tutorial to be very helpful: https://www.youtube.com/watch?v=YPItfQ87qjM&t=108s
#Keep in mind there are likely many other ways to do this. This is just one example.

