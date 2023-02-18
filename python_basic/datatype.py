
# Datatypes : - data + type

# it shows the type of our data 

# data type of types :

# 1. immutable : - doesnot change
#       1. tuple ()
#       2. string "" or '' 
# 2. mutable : - can change
#        1. list []
#        2. set {}
#        3. dict {key: value}



# imutable datatype: -

# ********************string : -*********************
 
# concept of string : string is collection of character 
# example: 
# a = "apple"
# b = "b"
c = "Happy Birthday"


# index = are two type:-
#     1. simple / dynamic(1.....end)
#     2. reverse index (-1 .....end)

# Note :- how to extraxt 't' from happy birthday ?

# print(c[9])
# print(c[13])

#  #reverse indexding

# print(c[-5])
# print(c[-10])

# # slicing :- extrating data from more than 1 index

# print(c[2:5])
# print(c[9:10+1])
# print(c[9:11])
# print(c[1:5])

# # slicing with reverse indexding

# # syntax: str_name[start: end+1]

# print(c[-8:-4])
# print(c[-10:-6+1])
# print(c[-10:-5])


#task:

# try to extract 'y b' with combination of reverse and simle indexing ---> task


# a[6] = i  this is give the error because string is immutable


# ********************TUPLE :- ***********************


# Difination :- collection of differente type and same of data is called Tuple

# tuple create by to type 
#    1. with bracket and
#     2. with out bracket .


# # syntax :- a = (x,y......)

# t = 100, 200, 300
# print(type(t))   # tuple

# # True = 1
# # False = 0

# tt = (123,'234',"apple",3234.23)
# print(type(tt))  # tuple

# print(tt[3])   # 3234.23
# print(tt[2])   # apple
# print(tt[1][2])  # 4
# print(tt[-3][-1])  # this also give the 4

# print(tt[1:3])    # ('234','apple')

# # tt[2] = 'dog'  # not change the value becuase tuple is not changeble

# # *******insert ***** in tuple

# # we can insert element using +

# ttt = tt+t      # insert in tuple is called concatenation ; 
# print(ttt)


# # *******************************   LIST ***************

# # mutable datatype : - we can change the data in mutable

# # List : - list is collection of different type of data type 

# # operation:-
# # we can perform indexing 
# # slicing 
# # update
# #insert


# # syntax :-  a[123,123,244,2, "ajay", 's']


# l = [110,'apple','cat',234.32,True,False]

# print(l[2])

# # update 

# l[2] = 'dog'  # because list is mutable
# print(l[2])

# # insert :- list_name.insert[index,value]

# l.insert(2,'dewari')

# print(l[2])

# print(l)

# # append : -  l.append(value)

# l.append(1234)
# print(l)

# # remove: -  list_name.remove('value')

# l.remove('dewari')

# print(l)

# # pop :- list_name.pop(index)

# l.pop(1)
# print(l)

# # Del :- del list_name[index]

# del l[4]
# print(l)



# # *********************** DICTIONARY ************

# # dictionary is a key value pair

# # value  



# d = {100:'ajay', 200: 3000, 300: 2.34}

# print(d.keys())  # keys 
# print(d.values())  # values

# # indexing in dict

# print(d[200])

# # slicing : no silicing in dictionary

# # UPDATING values in dict:-
# # syntax:- dict_name[key] = value

# d[100] = 'ajay singh'
# print(d)

# # INSERTING VALUE in dict :-

# d[400] = 'vijay'
# print(d)

# # DELETE VALUE  in dict :-

# del d[400]
# print(d)

# d.pop(100)
# print(d)

# # d.remove(3000)
# # print(d)  # remove is not work for dictionaryh


           

# task :-

# take a t = (90,'how','good', True) -> extract w from how , u from true ,90

t = (90,'how ','good',True)
print(t[1][2]) # w

print(t[3])  # True is extractable but in True, u is not extractable beacause True is one single keyword for 1

print(t[0])   # 90


# create a dictionary as a cloth seller

seller = {
    # price : item
    200 : 't_shirt',
    350 : 'shirt',
    500 : 'jeans',
    400 : 'formal_paint'

}
print(seller[200])    # t_shirt

# try to extact 'y b' with combination of reverse and simle indexing ---> task

a = 'Happy birthday'

print(a[4:-7])    # combination of simple and reverse indexing    output:- y b



# **************SET*******************

# SET: set is collection of unorderd data type  data

#creation of set

s = {"apple",123,23,'mango',True,0}

print(s)   # output : {0, True, 'apple', 23, 123, 'mango'}

s1 = {5,6,2,4,65,45,0}
print(s1)  # output: {0, 65, 2, 4, 5, 6, 45}

#Note:- we cannot able to do indexing and slicing in set
# print(s1[2])   # error : set is not subscriptable

# insert element into set

s.add(100)
print(s)

# delete element from set

s.remove(100)
print(s)

# remove duplicate 

s2 = {1,2,3,4,3,}
print(s2)

















