from random import *


start = int(input("Минимальное число диапазона: "))
finish = int(input("Максимальное число диапазона: "))
secret_number = randint(start, finish)
input_number = int
counter = 0


while secret_number != input_number:
    counter += 1
    input_number = int(input("Введите число: "))
    if secret_number > input_number:
        print("Число меньше, чем нужно. Попробуйте ещё раз!")
    elif secret_number < input_number:
        print("Число больше, чем нужно. Попробуйте ещё раз!")

print(secret_number)
