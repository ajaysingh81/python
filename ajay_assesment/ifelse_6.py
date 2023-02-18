
n = int(input("Enter a number for checking Greater,Armstrong,Prime :- "))

if True:
    if n>=100:
        print("Number is greater")
    else:
        print("Number is not greater")

if True:
    rem = 0
    sum = 0
    temp = n
    while(temp>0):
        rem = int(temp%10)
        sum = sum + (rem*rem*rem)
        temp = int(temp/10)

    if n == sum:
        print("Number is armstrong ")
    else:
        print("Number is not armstrong")

if True:
    flag = 0
    for i in range(2,n):
        if(n%i== 0):
            flag = 1
    
    if flag == 0:
        print("number is prime")
    else:
        print("number is not prime")
