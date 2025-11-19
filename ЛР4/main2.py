# TODO импортировать необходимые модули

import csv
import json
import io

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    data_list = []
    try:
        with open(INPUT_FILENAME, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                data_list.append(row)
    except FileNotFoundError:
        print(f"Ошибка: Файл '{INPUT_FILENAME}' не найден.")
        return

    # TODO считать содержимое csv файла

    try:
        with open(OUTPUT_FILENAME, mode='w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Ошибка записи в файл '{OUTPUT_FILENAME}': {e}")

    # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME, encoding="utf-8") as output_f:
        for line in output_f:
            print(line, end="")
