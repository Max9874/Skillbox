temperary_desyatki = 0
temperary_edenici = 0


for number in range(10, 101):
    temperary_desyatki = number // 10
    temperary_edenici = number % 10
    if number == 3 * (temperary_desyatki * temperary_edenici):
        print(number)
    
