# # literals = a literal is a value assigned to a variable

# # Type of Literal 

# # int , float , bool , string 

# a = 123   # integer literal 
# print(type(a))
# print(a)

# b = 234.34   # float literal
# print(type(b))
# print(b)

# c = "How are you"  #string literal
# print(type(c))
# print(c)

# d = True   # bool literal
# print(type(d))
# print(d)

# e = 'a'  # this is also is string literal
# print(type(e))
# print(e)


# #  difference ways of assigning a variable 
# #1. static 
# #2. dynamic


# print("static assignment")
# a = 123
# b = 23.23
# c = 'hi'
# d = False
# print(a,b,c,d)

# print("Dynamic assignment")
# # Dynamic assignment : - value given in run time 

# # this task is done by using input() keyword

# #Note : - default type of input funtion is string

# dd = input()
# print(dd)

# name = input("Enter your name") 
# print(name)

# # why we need daynamic input when we have static

# # take a example of calculater

# #  it take all value which you want calculate and give you responce according to your operation 

# # Note : - anything which is in single quotation '' and double quotation  "" called as string 

# # string : string is a collection of word

# #example : "Ajay singh rathor" , 'ram is back'

# print("concatenation")

# a = 'good '
# b = 'morning'
# print(a+b)  # this is called as concatination (+) here + is concatenation symbol


# # Note : in string , we can not perform add the value

# a = 10 
# a1 = 20
# print(a + a1)  # addition

# b = 'hii'
# c = 'ajay'
# print(b + c)  # concatination

# aa = input("Enter your name -")

# print(aa)
# print(type(aa)) # type is string

# #Note : - default type of input funtion is string

# # HOW to fix this?

# # we can fix this with the help fo type casting 

# # type casting : - changing one datatype to another data type is called type casting 

# # int() -> to type cast to integer
# # float() -> to typecast to float
# # str() -> to typecast to string
# # Bool() -> to typecast to string

# a = 10 
# a = float(a)
# print(type(a)) # float

# b = 123.23
# b  = int(b) 
# print(type(b)) # int

# c = 235
# c = str(c)
# print(type(c))  # str

# aaa = input("Enter your Phone number")
# print(type(aaa))  # default data type is string 
# print(aaa)

# a = int(input("Enter your phone number "))  
# print(type(a))  # datatype is int 
# print(a)



# task :-

# wap using user defined(input()) add 2 numbers

aaaa = int(input("Enter your first number:- "))
bbbb = int(input("Enter your second number:- "))
cccc = aaaa+bbbb
print("Result is:- ",cccc)

# write a program to ask the user to enter his details like name, phone numer and age (the datatypes should match)

name = input("Enter your name :- ")
age = int(input("Enter your age :- "))
phone_number = int(input("Enter your phone number :- "))

print("Your name is :- ",name)
print("Your age is :- ",age)
print("Your Phone Number is :-",phone_number)

