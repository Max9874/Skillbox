perfect = 0
good = 0
avarage = 0
amount_of_numbers = int(input("Кол-во оценок: "))

for i in range(1, amount_of_numbers + 1):
	students_ocenka = int(input(f"Оценка студента n{i}: "))
	if students_ocenka == 5:
		perfect += 1
	elif students_ocenka == 4:
		good += 1
	elif students_ocenka == 3:
		avarage += 1
print(perfect, good, avarage)
