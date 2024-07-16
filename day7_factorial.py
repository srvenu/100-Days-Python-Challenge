# day7_Factorial
def factorial(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        return num*factorial(num-1)
    
num=-1
while num < 0:
    num=int(input("Enter Positive number : "))

print(num)

print(f"Factorial of {num} is : {factorial(num)}")