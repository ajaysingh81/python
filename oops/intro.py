# *************************** INTRODUCTION OF OOP'S  :-  ****************

# 1. Object :- Object is member of class.

# object_name = class_name()

# 2. Class :- Class is blueprint for any object.
# class is discription of object

# how to create class

# Class class_name:
    # body


# 3. mathod :- mathod obtain property of object
    
# def mathod_name(self,parameters):
#     body


# flow of oops programe:

# create class:
# create mathod inside class
# create object for the class


# example:
# Class class_name:
#      def method_name(self, parameters):
#         body

# object_name = class_name()


# class add:
#     def sum(self,a,b):
#         print(f"sum is { a+b}")
#         print("sum is {0} and {1} is {2}".format(a,b,a+b))

# obj = add()
# obj.sum(23,30)


# class house:
#     def sleep(self):
#         print("this is the room")

#     def tv(self):
#         print("this is the living room")

#     def cook(self):
#         print("this is the kitchen room")
#     def guest(self):
#         print("this is the hall")

# obj = house()   # object creation of class

# obj.cook()    # calling of the mathod
# obj.guest()
# obj.tv()
# obj.sleep()

    
# task:-
# 1. write a code using class and object to calculate numbers 


# class calculator:
#     def add(self,a,b):
#         print(a+b)
#     def mul(self,a,b):
#         print(a*b)
#     def div(self,a,b):
#         print(a/b)
#     def sub(self,a,b):
#         print(a-b)
#     def mod(self,a,b):
#         print(a%b)

# obj = calculator()
# obj.add(12,23)
# obj.mul(23,43)
# obj.div(12,34)
# obj.mod(33,11)
# obj.sub(23,43)



# Self :- what is the self
# self is a permission for entering the class

class demo:
    def add(self,a,b):
        print(a+b)
o = demo()
o.add(2,3)

#task:-

# exel/word/natepad all syntax (basic +opps) make al table and / write all syntax  --- this is a mandotory task

## create a user defined function to add n number off integers.---> task 

# def add_multiple_values(l):
#     sum = 0
#     for i in l:
#         sum = sum + i

#     return sum

# n = int(input("enter how many value you want to add :-"))
# l = []
# for i in range(0,n):
#     a = int(input("Enter the value:- "))
#     l.append(a)

# result = add_multiple_values(l)
# print("RESULT IS :- ",result)


#*********  2nd way *************

def add(*a):
    print(sum(a))
add(1,2,4,3,2,4)


# ********************* 3rd way ***************



    