money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

current_money = money_capital
current_spend = spend
mounths = 0

while True:
    budget = current_money + salary
    if current_spend > budget:
        break
    current_money = budget - current_spend
    mounths += 1
    if mounths >= 1:
        current_spend *= (1 + increase)

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:", mounths)

