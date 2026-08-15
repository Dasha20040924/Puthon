lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

# Вывод элементов, которые меньше 30 и делятся на 3
for element in lst:
    if element < 30 and element % 3 == 0:
        print(element)
