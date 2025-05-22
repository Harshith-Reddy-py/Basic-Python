a = int(input("Give one Number: "))
c = input("Give the operation to be performed(+,-,*,/): ")
b = int(input("Give another number: "))
if   c == "+":
        print(f"The sum is:{a+b}")
elif c == "-":
        print(f"The difference is:{a-b}")
elif c == "*":
        print(f"The product is:{a*b}")
elif b==0 and c=="/":
        print("Division by zero is undefined")
elif c == "/":
        print(f"The quotient is:{a/b}")
else: 
        print("INVALID operator")
