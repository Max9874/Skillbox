height = int(input("Height: "))
space = 1
number = 1


for _ in range(height):
    space += 3

for row in range(1, height + 1):
    print(space * " ", end="")
    for col in range(row):
        print(number, "    ", end="")
        number += 2
    space -= 3
    print()
