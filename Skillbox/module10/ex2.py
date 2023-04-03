N_amount_of_levels = int(input("Enter number: "))


for element in range(1, N_amount_of_levels + 1):
    for amount in range(element):
        print(element, end=" ")
    print()
