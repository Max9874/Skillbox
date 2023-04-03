text = input("Введите зашифрованое сообщение: ")

result = ""
start = ""
finish = ""
counter = 1

for symbol in text:
    if counter % 2 == 1:
        start += symbol
    else:
        finish += symbol
    counter += 1
finish = "".join(reversed(finish))
result = start + finish
print(result)

