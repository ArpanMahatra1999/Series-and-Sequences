def fib(n):
    if n==0:
        result = 0
    elif n==1:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    return result

n = input("Enter the how much values of fibonacci numbers is required: ")

print("The fibonacci number at ",n," : ",fib(int(n)))