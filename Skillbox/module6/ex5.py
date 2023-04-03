houre = 0
counter_for_wifes_calls = 0
counter_for_opgaver = 0

print("Начался восьмичасовой рабочий день.")
    
    
while True:
    houre += 1
    if houre > 8:
        break
    print(f"{houre}-й час")
    counter_for_opgaver += int(input("Сколько "
                    "задач решит Максим? "))
    counter_for_wifes_calls += int(input("Звонит жена. Взять трубку? (1 — да, 0 — нет):"))
    
    
print(f"Рабочий день закончился. Всего выполнено задач:{counter_for_opgaver}")

if counter_for_wifes_calls > 0:
    print("Нужно зайти в магазин!")
