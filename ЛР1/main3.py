list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

middle = len(list_players) // 2

team_1 = list_players[:middle]
team_2 = list_players[middle:]

print(team_1, team_2, sep="\n")