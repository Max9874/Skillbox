number = 600851475143
devider = 1
list_of_deviders = []
result = 0

while number != 1:
    if number % devider == 0:
        number /= devider
        list_of_deviders.append(devider)
    devider += 1

for candidate in list_of_deviders:
    if candidate > result:
        result = candidate

print(list_of_deviders)
print(f"Наибольшее простое число делитель для данного числа - это {result}")
