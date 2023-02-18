#********************* INHERITANCE *********************

# taking data from parent class ---> inheritance

# note:  child can access all function and all thing from parent but parent cannot accesa parent data 


#TYPE:

# 1.single inheritance
# 2.multilevel inheritance
# 3.multiple inheritance


# ***************** SINGLE INHERITANCE ******************

# def:- single child class inherited for single parent class


# SYNTAX;-

# class parent:
#     body

# class child(parent):
#     body


# class parent:
#     def pm(self):
#         print("this is parent class")

# class child(parent):
#     def cm(self):
#         print("this is child class")

# """p = parent() 
# p.pm()
# c = child()
# c.cm()"""

# cp = child()   # object creation of child class
# cp.cm()   # access child class 
# cp.pm()    # acces parent class



#************************** MULTIPLEVEL INHERITANCE ******************

# SYNTAX:-
# class grantdparent:
#     body
# class parant(grantdparent
# ):
#     body
# class child(parent):
#     body



class gp:
    def gpm(self):
        print("This is the grandparent class")
class parent(gp):
    def pm(self):
        print("this is the parent class")
class child(parent):
    def cm(self):
        print("this is the parent class")




c = child()
c.gpm()
c.pm()
c.cm()


# **************************** Multiple Inheritance ***************************

#syntax:-
# class parent1:
#     body

# class paraent2:
#     body

# class child:
#     body


class parent1:
    def p1(self):
        print("this is parent1 class")

class paraent2:
    def p2(self):
        print("this is parent2 class")

class child(parent1,paraent2):
    def cm(self):
        print("this is child class")

p1 = parent1()
p2 = paraent2()
c = child()

c.p1()
c.p2()