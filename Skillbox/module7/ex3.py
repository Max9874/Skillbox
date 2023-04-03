n_number = int(input("Найти факториал числа: "))
summary = 1


for num in range(1,n_number + 1):
    summary *= num

print(summary, "- Факториал числа", n_number)
