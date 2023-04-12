# Яма

deep = int(input("Deep: "))
counter = deep * 2
number_sequence = ""

for row in range(deep + 1):

    for col1 in range(row):
        print(deep - col1, end="")

    if counter != deep * 2:
        print(counter * ".", end="")

    for col2 in range(row):
        number_sequence += str(deep - col2)

    number_sequence = number_sequence[::-1]

    print(number_sequence, end="")

    number_sequence = ""
    counter -= 2
    print()
