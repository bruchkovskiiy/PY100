# Получение числа от пользователя
def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            if number.is_integer():
                return int(number)
            return number
        except ValueError:
            print("Ошибка: Некорректное значение. Пожалуйста, введите число.")


# Получение математического оператора
def get_operation():

    correct_operations = '+-/*'
    operation = input("Выберете математическую операцию (+ - / *): ")

    while operation not in correct_operations:
        print('Выберете операцию из списка.')
        operation = input("Выберете математическую операцию (+ - / *): ")
    return operation


# Вычисление операции
def calculate(number_1, number_2, operation):
    result = None
    if operation == '+':
        result = number_1 + number_2
    elif operation == '-':
        result = number_1 - number_2
    elif operation == '/':
        try:
            result = number_1 / number_2
        except ZeroDivisionError:
            result = "Ошибка: Деление на ноль невозможно."
    elif operation == '*':
        result = number_1 * number_2
    return result


# Главная функция, которая включает в себя остальные функции
def main():
    print("Привет! Это простой калькулятор с основными операциями.")
    number_1 = get_number("Введите первое число: ")
    number_2 = get_number("Введите второе число: ")
    operation = get_operation()
    result = calculate(number_1, number_2, operation)
    print("Результат:", result)


# Запуск программы
if __name__ == "__main__":
    main()

