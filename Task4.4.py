import random
k = int(input("Введите натуральное число k: "))
polynom = ''
for i in range(k, -1, -1):
    coef = random.randint(0, 100)
    if i > 1:
        polynom += str(coef) + '*x' + '^' + str(i)
        polynom += '+'
    elif i > 0:
        polynom += str(coef) + 'x'
        polynom += '+'
    else:
        polynom += str(coef)
polynom += '=0'
text = open('file_polynom.txt', 'w')
text.write(polynom)
text.close()