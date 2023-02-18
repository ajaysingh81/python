# ######################################  Inheritance ################################

# main class
class first:
    print("This is a main function")
    a=35
    def func(self):
        print("This is a main class mathod")

# derived class
class child(first):   # make a derived class and inherite main class
    def __init__(self,b):
        self.b =b

    def sum(self):
        return self.a + self.b

sum1 = child(4)    # object creation 
sum1.func()      # calling main class function
result = sum1.sum()  
print(result)



# ##########################    Inheritance 2 ############################

class size:
    def ___init__(self):
        self.b = 0
        self.h = 0


class trigleArea(size):
    pi = 3.137
    def tringleCal(self):
        a = float(1/2*(self.b * self.h))
        return a

# obj = trigleArea()

# obj.b = 10
# obj.h = 223                                        ## single inheritance

# result = obj.tringleCal()
# print(result)


class circleArea(trigleArea):
    def circlCal(self):
        ci = 2 * self.pi * self.b
        return ci


# obj = circleArea()

# obj.b = 3                                          ## multilavel inheritance

# result = obj.circlCal()
# print(result)
