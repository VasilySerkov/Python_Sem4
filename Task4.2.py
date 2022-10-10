number = int(input(f"Введите натуральное число N: "))
prime_mltpls = []
for i in range(2, number):
    if number % i == 0:
        count = 1
        for j in range(2, i//2 +1):
            if i % j == 0:
                count = 0
                break
        if count == 1:
            prime_mltpls.append(i)
print(prime_mltpls)