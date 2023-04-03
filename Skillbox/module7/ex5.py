a_number = int(input("A: "))
b_number = int(input("B: "))
counter = 0
summary = 0


if a_number > b_number:
        temperary_c = a_number
        a_number = b_number
        b_number = temperary_c
        print(a_number, b_number)


for number in range(a_number, b_number + 1):
    if number % 3 == 0:
        counter += 1
        summary += number
        print(number)
print(summary / counter)
    
