reverse_timer = int(input("На сколько секунд установим таймер?: "))
reverse_timer_second = reverse_timer + 1


for second in range(1, reverse_timer + 2):
    reverse_timer_second -= 1

    if reverse_timer_second == 0:
        print("Ваша еда готова, осторожно - горячо.")
        break
    
    print(reverse_timer_second, "секунда")

    off_button = int(input("1 - закончить программу, 0 - продолжить исполнение програмы: "))
    if off_button == 1:
        print("Ваша еда готова.", revesre_timer_second)
        break
    
        
