def check_prime(x):
    if x==1 or x==0:
        return 0
    elif x==2:
        return 1
    elif x>2:
        for i in range(2,x):
            if x%i == 0:
                return 0
                break
            else:
                return 1

num=int(input("Enter a number : "))
flag = check_prime(num)

if flag == 1:
    print(f'{num} is Prime.')
else:
    print(f'{num} is not Prime.')
