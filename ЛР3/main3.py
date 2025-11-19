def count_letters(text: str) -> dict:
    counts = {}
    text_lower = text.lower()
    for char in text_lower:
        if char.isalpha():
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1

    return counts


    """
    Функция возвращает словарь котором ключи это буквы нижнего регистра полученные из text,
    а значение это сколько раз эта буква встретилась в text.

    пример:
        text = 'У лукоморья дуб зелёный;'
        result = count_letters(text)
        print(result)  # {'у': 3, 'л': 2, 'к': 1, 'о': 2, 'м': 1, 'р': 1, 'ь': 1, 'я': 1, 'д': 1, 'б': 1, 'з': 1,
        'е': 1, 'ё': 1, 'н': 1, 'ы': 1, 'й': 1}
    """
    letter_counts_dict = count_letters(sample_text)  # TODO Реализуйте функцию


def calculate_frequency(letter_count: dict) -> dict:
    total_letters = sum(letter_count.values())
    frequencies = {}
    for letter, count in letter_count.items():
        if total_letters > 0:
            frequency = count / total_letters
            frequencies[letter] = frequency
        else:
            frequencies[letter] = 0.0

    return frequencies


    """
    Функция возвращает словарь, где буква используется как ключ, а ее частота как значение.

    пример:
        letter_count = {'у': 3, 'л': 2, 'к': 1, 'о': 2, 'м': 1, 'р': 1, 'ь': 1, 'я': 1, 'д': 1, 'б': 1, 'з': 1,
        'е': 1, 'ё': 1, 'н': 1, 'ы': 1, 'й': 1}
        result = calculate_frequency(letter_count)
        print(result)  # {'у': 0.15, 'л': 0.1, 'к': 0.05, 'о': 0.1, 'м': 0.05, 'р': 0.05, 'ь': 0.05, 'я': 0.05,
        'д': 0.05, 'б': 0.05, 'з': 0.05, 'е': 0.05, 'ё': 0.05, 'н': 0.05, 'ы': 0.05, 'й': 0.05}
    """
    frequency_dict = calculate_frequency(letter_counts_dict)  # TODO Реализуйте функцию


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

count_dict = count_letters(main_str)
frequency_dict = calculate_frequency(count_dict)

# TODO Распечатайте в столбик букву и её частоту в тексте

for letter, frequency in frequency_dict.items():
    print(f"{letter}: {frequency:.2f}")