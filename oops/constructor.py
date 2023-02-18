# ****************** CONSTRUCTOR ************************

# This a special mathod
# this is initilize when object was created

# Types:-

# 1. default constructor / non parameter 
# 2. parameterised constructor 

# syntax:- 

# def __init__(self):
#     body



#*************************DEFAULT CONSTRUCTOR ***************************

# wap for adding to number using constructor

# default constructor and no parameter 

class demo:
    def __init__(self):
        self.a = 10
        self.b = 10
        print("object successfully completed and contuctor is called")

    def sum(self):
        print(self.a+self.b)

o = demo()
o.sum()


# ****************************** PARAMETERIZED CONSTRUCTOR **********************

class c:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print("object created and contructo activated")

        print("value of a",a)
        print("vlaue of b",b)

    def add(self):
        print(self.a+self.b)

o = c(6,11)
o.add()  

    