def calculator(a,b,op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    elif op == '/':
        if b != 0:
            return a/b
        else:
            print("Division by Zero Errror")
    else:
        print("Enter valid operator")

def get_input():
    a=int(input("Enter number 1 : "))
    b=int(input("Enter number 2 : "))
    op=input("Enter the operator + - * or / : ")
    print(f"The result is {a} {op} {b} = {calculator(a,b,op)}")
    con=input("Do you want to continue yes or no : ")
    if con.lower() == 'yes':
        calculate=True
    else:
        calculate=False
    
    return calculate

calculate=True

while calculate:
    if calculate==True:
        calculate=get_input()
    else:
        break
        
