numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

slice_of_numbers_1 = numbers[:4]
slice_of_numbers_2 = numbers[5:]

sum_of_numbers_1 = sum(slice_of_numbers_1)
sum_of_numbers_2 = sum(slice_of_numbers_2)

sum_of_all_numbers = sum_of_numbers_1 + sum_of_numbers_2
all_the_numbers = len(numbers)
arithmetic_mean = sum_of_all_numbers / all_the_numbers

numbers[4] = arithmetic_mean

# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
