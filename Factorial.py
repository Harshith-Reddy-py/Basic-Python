#Finding factorial for given input
try:
    num = int(input("Enter a non-negative integer: "))

    if num < 0:
            print("Factorial is not defined for negative numbers.")
    elif num == 0:
            print(f"The factorial of 0 is: 1")
    else:
        factorial = 1
    for i in range(1, num + 1):
        factorial *= i  
    print(f"The factorial of {num} is: {factorial}")
except ValueError:
        print("Invalid input. Please enter an integer.")
