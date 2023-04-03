food_counter = 100


for month in range(1, 100):
    if food_counter > 3:
        print(f"{month}-й месяц. Еды осталось:")
        food_counter -= 4
        print(f"{food_counter} кг.")
    else:
        print(f"{month} месяцев сможет прожить этот чупачупс.")
        break
