amount_of_numbers = int(input("enter amount of numbers: "))
divider = 2
counter = 0


def is_prime(number):
    local_divider = 2
    while number % local_divider != 0:
        local_divider += 1
    if local_divider == number:
        return True


for _ in range(amount_of_numbers):
    checking_number = int(input("Enter number: "))
    if is_prime(checking_number):
        counter += 1

print(f"Количество простых чисел - {counter}")
