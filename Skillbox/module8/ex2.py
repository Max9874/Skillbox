amount_of_dolgniki = int(input("Сколько должников в списке: "))
row_counter = 0
dolg = 0

for number in range(1, amount_of_dolgniki + 1):
    row_counter += 1

    if row_counter % 5 == 0:
        print(f"Должник номер {row_counter}")
        dolg += int(input(f"Сколько денег вы должны?: \n"))

print(dolg)
