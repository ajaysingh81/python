# n = int(input("Enter how many even no. you want :- "))

l = []
for i in range(1,2*50+1):
    if i%2 == 0:
        l.append(i)

print(l)

# count the number of element in list
print(len(l))

# reverse the sequence of list
l.reverse()
print(l)

# sort the list acending and decending order

l.sort(reverse = True)  # decending order
print(l)

l.sort()   # acending order
print(l)


# get the element 44 th index
print(l[44-1])

#update
l[44-1] = 100

print(l)

# square 
l1 = []
for i in l:
    l1.append(i*i)
print(l1)