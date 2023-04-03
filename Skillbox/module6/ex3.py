number = int(input("Indset number:"))
counter = 0
while True:
    if number % 10 > 0:
        number = number // 10
        print(number)
        counter += 1
    else:
        break
print(counter)
