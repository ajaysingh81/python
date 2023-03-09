n = int(input("Enter the number for checking greater , armstrong and prime  "))

if n>9:
    print("given number is greater")
else:
    print("given number is not greater ")



# for checking armstrong or not

sum = 0 
rem = 0 
temp = n
while(temp>0):
    rem = temp % 10 
    sum = sum + (rem**3)
    temp = int(temp/10)
  
if temp == n:
    print("given number is armstrong ")

else:
    print("given number is not armstrong")


# for checking the prime or not

flag = 0
for i in range(2,n):
    if n%i == 0:
        flag = 1

if flag == 0:
    print("given number is prime")
else:
    print("given no.is not a prime number")

