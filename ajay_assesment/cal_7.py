n = int(input("Enter a first value - "))

m = int(input("Enter a second value - "))

op = input("Enter a operator(+,-,*,/,//) ")

if op == "+":
    print("sum is :-",n+m)

elif op == "-":
    print("sub is :-",n-m)

elif op == "*":
    print("mul is :-",n*m)

elif op == "/":
    print("division is :-",n/m)

elif op == "//":
    print("floor division is :-",n//m)


else:
    print("Please! Enter valid operatorn")