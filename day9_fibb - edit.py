def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return num+fib(num-1)
    
num=int(input("Enter number : "))
print(fib(num))