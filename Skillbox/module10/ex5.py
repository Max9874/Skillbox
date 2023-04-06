amount_of_numbers = int(input("Количество чисел: "))
result = 0
summary = 0

for _ in range(amount_of_numbers):
    number = int(input("Введите число: "))
    for numeral in str(number):
        summary += int(numeral)
    if result < summary:
        result = summary
    summary = 0
print("{0} - самая большая сумма цифр.".format(result))
