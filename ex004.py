'''
# Показать числа, у которых
 последняя цифра делится на 4

'''


n = int(input("n = "))
for index in range(n + 1):
    if (index % 10) % 4 == 0:
        print(index, end=" ")
