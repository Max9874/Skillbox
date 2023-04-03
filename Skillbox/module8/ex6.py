educational_grant = int(input("Введите стипендию: "))
expenses = int(input("Введите аренду: "))
amount_of_money = 0


for month in range(1,11):
    ikkenok = round(expenses - educational_grant)
    print(f"{month}.месяц траты", end=" ")
    print(f"{expenses} не хватает {ikkenok}")
    amount_of_money += ikkenok
    expenses += round(expenses * 0.03)
print(amount_of_money)
    
