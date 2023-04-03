N_card = int(input("N: "))
summary = 0


for card in range(1, 1 + N_card):
    summary += card


    
for _ in range(N_card - 1):
    number = int(input("Карта: "))
    summary -= number
print(f"Пропавшая карта: {summary}")
