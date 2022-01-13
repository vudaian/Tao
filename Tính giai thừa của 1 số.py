def Factorial(n):
    factorial = 1
    if(n==0 or n==1):
        print("Factorial of ", n, "is 1!")
    else:
        for i in range(2, n + 1):
            factorial = factorial * i
        print("Factorial of", n, "is", factorial)
        
n = int(input("Enter the number to calculate the factorial: "))
Factorial(n)