def fibonacci(n):
    f0 = 0;
    f1 = 1;
    fn = 1; 
 
    if (n < 0):
        return -1;
    elif (n == 0 or n == 1):
        return n;
    else:
        for i in range(2, n):
            f0 = f1;
            f1 = fn;    
            fn = f0 + f1;
        return fn;
x=int(input("Nhập số phần tử của dãy số: "))
print(x , " số đầu tiên của dãy số fibonacci: ");
sb = "";
for i in range(0, x):
    sb = sb + str(fibonacci(i)) + "   ";
print(sb)