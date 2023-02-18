#CONDITIONAL STATEMENT:-

# flow control statement which alow us to do certain task with the condition


# type : -

# 1. if-else
# 2. if -elif-else
# 3. nested if-else

#************************** IF-ELSE***********
#  syntax :-

# IF condition:
#     STATEMENT 1
#     statment n 

# else: 
#     statement1 
#     statment n 

# note: 
# 1. indentation is must
# 2. (:)colomn is also must after if or else 

road = input("is the road blocked?")
if road =='blocked':
    print("go with the other root")

else: 
    print("Road is not blocked")



#***************************IF-ELIF-ELSE***************************

# syntax:-

# if condition:
#     statement1
# elif condition:
#     statement
# else:
#     statment


if road == "blocked":
    print("go with the other route")

elif road == "part":
    print("road is partially blocked you can go this road")

else:
    print("you can go this route")



# *********************** NESTED IF-ELSE********************


# SYNTAX:-

# if condition:
#     statement
#     if condition:
#         statement
#     else:
#         statement
# else:
#     statement


n = int(input("Enter a no. :-"))

if n>=0:
    if n==0:
        print("number is not positive but zero")
    else:
        print("number is positive")
else:
    print("number is not positive")