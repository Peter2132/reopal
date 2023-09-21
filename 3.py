number12 = int(input("Введите число: "))
sum = 0

while number12 > 0:
    digit = number12 % 10
    sum += digit
    number12 //= 10

print("Сумма цифр числа:", sum)