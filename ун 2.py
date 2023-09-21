def is_even(number12):
    return number12 % 2 == 0
while True:
    number12 = int(input("Введите число: "))
    if is_even(number12): 
     true = print(f"{number12} четное")
    else:
     false = print(f"{number12} не четное")
     break