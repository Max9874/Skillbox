"""
Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2,
первые 10 элементов будут:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.

"""
number = 1
previous_number = 1
previous_previous_number = 0
counter = 0
summary = 0

while number < 4000000:
    if number % 2 == 0:
        summary += number

    counter += 1

    if counter % 2 == 1:
        previous_previous_number = number
    elif counter % 2 == 0:
        previous_number = number

    number = previous_previous_number + previous_number

print(summary)
