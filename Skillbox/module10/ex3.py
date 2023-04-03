height = int(input("Введите высоту рамки: "))
width = int(input("Введите ширину рамки: "))
for col in range(height):
    for row in range(width):
        if col == 0 or col == height - 1:
            if row == 0 or row == width - 1:
                print("|", end="")
            else:
                print("-", end="")
        elif row == 0 or row == width - 1:
            print("|", end="")
        else:
            print(" ", end="")
    print()

