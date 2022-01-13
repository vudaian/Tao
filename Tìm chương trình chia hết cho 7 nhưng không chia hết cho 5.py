print("Những số chia hết cho 7 nhưng không chia hết cho 5 là: ")
for index in range(10, 201, 1):
    if (index % 7 == 0) and (index % 5 != 0):
        print(index, end= "   ")