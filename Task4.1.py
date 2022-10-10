decimal_precision = float((input(f"Введите заданную точность d: ")))
from math import pi
print(f'pi->, {int(pi / decimal_precision) * decimal_precision}')