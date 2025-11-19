salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

current_spend = spend
expenses_for_the_entire_period = 0

for i in range(1, months + 1):
    if i == 1:
        current_spend = spend
    elif i > 1:
        current_spend = current_spend * (1 + increase)
    expenses_for_the_entire_period += current_spend

salaries_for_the_entire_period = salary * months

money_capital = expenses_for_the_entire_period - salaries_for_the_entire_period

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", f"{money_capital:.2f}")


