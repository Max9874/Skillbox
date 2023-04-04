amount_of_numbers = int(input("enter amount of numbers: "))
divider = 2
counter = 0


def is_prime(number):
    local_divider = 2
    while number % local_divider != 0:
        local_divider += 1
    return local_divider == number


for _ in range(amount_of_numbers):
    checking_number = int(input("Enter number: "))
    while divider <= checking_number:
        if checking_number % divider == 0 and checking_number == divider or checking_number == 1:
            counter += 1
        divider += 1

print(f"Количество простых чисел - {counter}")

# bag. need to correct
