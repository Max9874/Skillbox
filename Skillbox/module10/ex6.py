height = int(input("Height of triangle:"))
symbol = 1
counter = 0
spaces = height
for row in range(1, height + 1):
    print(" " * spaces, end="")
    for line in range(row):
        print("#", end="")
    print(counter * "#", "\n", end="")
    counter += 1
    spaces -= 1
