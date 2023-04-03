number = int
counter = 0


for time in range(10):
    number = int(input("Введите число: "))
    if number % 2 == 0 and number > 0:
        counter += 1
print(counter)
