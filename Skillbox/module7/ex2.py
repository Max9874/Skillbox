money = 0
for month in range(1, 13):
    print(f"Месяц N{month}")
    money += int(input("Зарплата за месяц: "))
print("Зарплата за год:", money)
