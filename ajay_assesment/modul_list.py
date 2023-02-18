# module :- container having th predefined functionality for performing task related to different segment available

# ex.=  calculator , data maniputation operator , data visulaization , statistics model or machine learnig 

# A module may contain variables, functions, classes etc. Let's see an example,

# Let us create a module. Type the following and save it as module_list.py

# lirbrary:- 
# pandas
# matplotlib
# plotly
# sklearn
# seabarn
# scipy


# # Python Module addition

def add(a, b):
   result = a + b
   return result



x = [78,150,56,89,45,120]
print(x)
print(type(x))

# calculate the average of the x
sum = 0 
for i in x:
    sum = sum + i
mean = sum/len(x)

# output formating
print("Mean is :- {0}".format(mean))
print("Mean is :- %0.4f " %mean)
print("mean is :- {0:0.2f}".format(mean))

# 2nd way using module which is numpy
import numpy as np
xn = [23,45,22,34,54,34]
m = np.mean(xn)

print("Mean is (2nd way) :-",m)

# take a input using map funtion
n = list(map(int,input("Enter the no. in list :-").split(",")))
print(n)
