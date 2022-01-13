import math
def PTbac2(a, b, c):
    if (a == 0):
        if (b == 0):
            print ("The equation has no solution!")
        else:
            print ("The equation has a solution: x = ", + (-c / b))
        return
    d = b * b - 4 * a * c
    if (d > 0):
        x1 = (float)((-b + math.sqrt(d)) / (2 * a))
        x2 = (float)((-b - math.sqrt(d)) / (2 * a))
        print ("The equation with 2 solutions: x1 = ", x1, " và x2 = ", x2)
    elif (d == 0):
        x1 = (-b / (2 * a))
        print("Equation with double roots: x1 = x2 = ", x1)
    else:
        print("The equation has no solution!")
        
a = int(input("Import a = "))
b = int(input("Import b = "))
c = int(input("Import c = "))
PTbac2(a, b, c)