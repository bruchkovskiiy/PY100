# TODO Найдите количество книг, которое можно разместить на дискете

in_one_book = 4 * 25 * 50 * 100
floppy_disk_capacity = 1.44 * 1024 * 1024
number_of_books = floppy_disk_capacity / in_one_book

print("Количество книг, помещающихся на дискету:", int(number_of_books))

