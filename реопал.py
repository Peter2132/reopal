import math

def summa(first, second):
    return first + second

def sub(first, second):
    return first - second

def mult(first, second):
    return first * second

def div(first, second):
    if second == 0:
        return 'Ошибка!' 
    return first / second

def calc(first, second, oper):
    operations = {
        '+': summa,
        '-': sub,
        '*': mult,
        '/': div,
        '%': lambda x, y: x / y * 100,
        '**': lambda x, y: x ** y,
        '√': lambda x, _: math.sqrt(x),
        '!': lambda x, _: math.factorial(x),
        'sin': lambda x, _: math.sin(x),
        'cos': lambda x, _: math.cos(x),
        'tan': lambda x, _: math.tan(x)
    }

    return operations.get(oper, lambda x, y: 'Такого действия не существует!')(first, second)

def operation():
    operation_descriptions = {
        '+': 'сумму',
        '-': 'разность',
        '*': 'умножение',
        '/': 'деление',
        '%': 'процента первого числа от второго',
        '**': 'возведение в степень',
        '√': 'квадратный корень первого числа',
        '!': 'факториал первого числа',
        'sin': 'синус первого числа',
        'cos': 'косинус первого числа',
        'tan': 'тангес первого числа'
    }

    while True:
        mes = input('Выберите операцию (Введите +, -, *, /, %, **, √, !, sin, cos, tan):\n')
        if mes in operation_descriptions:
            print("Вы выбрали: ")
            return mes
        else:
            print('Выбранной операции не существует!')

def get_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Такого числа не существует!')

def run():
    first = get_input('Введите первое число: ')
    second = get_input('Введите второе число: ')
    op = operation()
    result = calc(first, second, op)
    print(f'Результат: {result}')

if __name__ == '__main__':
    while True:
        run()
        answer = input('Работать дальше?\n Введите r если да, если нет Enter: ')
        if answer != 'r':
            break