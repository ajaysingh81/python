# # in python be use class keyword for creating the class 

# #********************** CLASS****************** inside mathod **********


# class add:
#     # constructor funtion
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b

#     def sum_(self,a = 4,b = 5):
#         # print("sum : ",self.a+self.b)
#         # print(a+b)
#         return self.a+self.b , a+b

# # when we use contructor in program that time give the in a variable  intilizatioon time

# s = add(23,34)    # object creation with value passing 
# s.sum_()                # method calling 
    
# sum = s.sum_()
# print("sum :",sum)     # return the tuple



# *************************** outside class *****************************

# class cs:
#     pass 

# def func(self):
#     print("function is running")

# cs.method = func(cs)   #calling function

# cs1 = cs()     # object creation


# other function

class motor:
    a = 6 

def gear(self):
    print(f"This is a {self.a}")

motor.mathod = gear(motor)

gadi = motor()

print(gadi.mathod)




