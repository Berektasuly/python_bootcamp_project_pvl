list = input("Введите числа через , вот пример: 1,2,3,4,5: ").split(",")
# Отсортируем список чисел через цикл
sorted_list = sorted([int(num) for num in list])
print("Отсортированный список чисел: ", sorted_list)