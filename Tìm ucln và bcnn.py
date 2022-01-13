def divisor(a, b):
    temp_a = a
    temp_b = b
    while (a != b):
        if (a > b):
            a -= b
        else:
            b -= a
    print("The greatest common divisor of", temp_a, "and", temp_b, "is: ",a)
def multiple(a, b):
    temp_multiple = (float)((a * b) / divisor(a, b))
    print("The least common multiple of", a, "and", b, "is:", temp_multiple)
    
a = int(input("Import a = "))
b = int(input("Import b = "))
multiple(a, b)
divisor(a, b)