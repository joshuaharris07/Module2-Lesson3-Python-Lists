# Advanced Slicing Techniques

#Problem Statement: You have a list of daily temperatures for one month, and you'd like to extract specific data from it.

#Task 1: Given the list of temperatures:
#temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
#Extract the temperatures for the second week (7 days) of the month (index 7 to index 14). 
#Expected Outcome: 83, 85, 86, 87, 88, 89, 90,

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
print(temperatures[7:14])


#Task 2: Extract all the temperatures above 100. 
# HINT: add the temperatures over 100 to a new list, or use list slicing to get the temperatures.

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
temperatures.sort()     #in case any of the data points aren't already in order.
temp_over_100 = temperatures[temperatures.index(100):]
print(temp_over_100)
