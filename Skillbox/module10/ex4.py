amount_of_numbers = int(input("enter amount of numbers: "))
divider = 2
counter = 0

for _ in range(amount_of_numbers):
    number = int(input("Enter number: "))
    while divider <= number:
        if number % divider == 0 and number == divider or number == 1:
            counter += 1
        divider += 1

print(f"Количество простых чисел - {counter}")

# bag. need to correct
