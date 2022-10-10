count = int(input("Введите количество элементов списка: "))
number_list = list()
number_list = [0] * count
for i in range(count):
    number_list[i] = input(f"Введите число {i+1}-й элемент списка: ")
    while not number_list[i].isdigit():
        number_list[i] = input("Вы ввели некорректное число. Повторите ввод: ")
    number_list[i] = int(number_list[i])
unic_numbers = list(set(number_list))
print(unic_numbers)