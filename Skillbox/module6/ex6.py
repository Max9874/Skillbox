depozit = int(input("X: "))
procent = int(input("P: "))
wanting_summary = int(input("Y: "))
years_counter = 0


while True:
    if wanting_summary < depozit:
        break
    if depozit / 100 * procent > 1:
        depozit = depozit + (depozit / 100 * procent)
        depozit //= 1
    elif depozit / 100 * procent < 1:
        depozit = depozit + (depozit / 100 * procent)
        
    print(depozit)
    years_counter += 1


print(f"Через {years_counter} лет депозит достигнет {wanting_summary}.")
