
# *********     INCAPSULATION     ***********

class room:
    def __init__(self):
        self.__roomtem = 22      # private variable

    def set_tem(self,a):
        self.__roomtem = a
    
    def get_temp(self):
        print(f"temperature is :- {self.__roomtem}")
    


ch = room()
ch.get_temp()

ch.roomtem = 23   # we cannot chage directely beacuase variable is private
ch.get_temp()

ch.set_tem(24)    # change the value
ch.get_temp()


class area:

    def __init__(self):
        self.__breadth = 0
        self.__height = 0
    
    def print_(self):
        print(self.__breadth,self.__height)

    def getBre(self):
        print(f"Breadth is {self.__breadth} \n Height is {self.__height}")

    def setBre(self ,b,c):
        self.__breadth = b
        self.__height = c

    def trigleArea(self):
        a = self.__breadth * self.__height
        print(f"Area of Tringle is {a}")

obj = area()
obj.getBre()
obj.trigleArea()

obj.setBre(34,34)
obj.getBre()
obj.trigleArea()

obj.breadth = 2
obj.height = 3
obj.getBre()
obj.trigleArea()
obj.print_()