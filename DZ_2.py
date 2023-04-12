import fractions
from math import gcd

result = None

first_fraction = input("Введите первую дробь\n")
a1 = int(first_fraction[0])
b1 = int(first_fraction[2])

second_fraction = input("Введите вторую дробь\n")
a2 = int(second_fraction[0])
b2 = int(second_fraction[2])

a_sum = a1 * b2 + a2 * b1
b_sum = b1 * b2
div = gcd(a_sum, b_sum)
a_sum //= div
b_sum //= div
if a_sum % b_sum == 0 and a_sum >= b_sum:
    result = a_sum // b_sum
else:
    result = f'{a_sum}/{b_sum}'

print(f"Сумма двух дробей равна {result}")
print(f"Проверка с помощью функции: {fractions.Fraction(a1, b1) + fractions.Fraction(a2, b2)}\n")

a_mult = a1 * a2
b_mult = b1 * b2
div = gcd(a_mult, b_mult)
a_mult //= div
b_mult //= div
if a_mult % b_mult == 0 and a_sum >= b_sum:
    result = a_mult // b_mult
else:
    result = f'{a_mult}/{b_mult}'

print(f"Результат умножения дробей: {result}")
print(f"Проверка с помощью функции: {fractions.Fraction(a1, b1) * fractions.Fraction(a2, b2)}")
