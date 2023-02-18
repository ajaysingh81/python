# type casting in datatype

#task :
# typecasting with set tuple and list ,dict 


# ************* tuple to other data type ******

t = (234,4,43,443,23443)

l = list(t)   #tuple to list
print(l)
print(type(l))

s = set(l)    # tuple to set
print(s)
print(type(s))

# tuple to string
st = str(l)
print(st)
print(type(st))

# tuple to dict

# d = dict(l)    --> this operation cannot to do because dict store key :value pair
# print(d)   


# ***************** LIST TO OTHER DATA TYPE *************

l = [12,32,43,'ajay',True]

s = set(l)    # list to set
print(s)
print(type(s))

t = tuple(l)    # list to tuple
print(t)
print(type(t))

st = str(l)     # list to string
print(st)
print(type(st))

# d = dict(l)    # cannot be changeble
# print(d)
# print(type(d))


# ***************** SET TO OTHER DATA TYPE***********************


s = {123,123,543,'aa',True,False}

l = list(s)   # set to list
print(l)
print(type(l))

t = tuple(s)    # set to tuple
print(t)
print(type(t))

st = str(s)     # set to string
print(st)
print(type(st))

# d = dict(s)    # can't be changeble
# print(d)
# print(type(d))



#**************** STRING TO OTHER DATATYPE ***************

a = 'Ajay singh rathor'

l = list(a)   # string to list
print(l)
print(type(l))

t = tuple(a)    # string to tuple
print(t)
print(type(t))

s = set(a)    # string t0 set
print(s)
print(type(s))

# d = dict(s)    # cannot update
# print(d)
# print(type(d))


# *********************** DICT TO OTHER DATATYPE ************


d = {100:"ajay",200:"vijay",300:True,400:False,500:5000,600:1234.2345}

l = list(d)   # dict to list  output is same as l.keys()
print(l)
print(type(l))   # type is list


t = tuple(d)   # dict to list
print(t)
print(type(t))

s = set(d)   # dict to set
print(s)
print(type(s))

st = str(d)   # dict to string
print(st)
print(type(st))








