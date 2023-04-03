x_line = 8
y_line = 10
operators_move = ""


print(f"Марсоход находится на позиции {x_line}, {y_line}, введите команду:")


while True:
    
    operators_move = input("Deside way to move: ").lower()
    if (y_line < 20) and (operators_move == "w"):
        y_line += 1
        print(f"Марсоход находится на позиции {x_line}, {y_line}, введите команду:")

    elif (y_line > 1) and (operators_move == "s"):
        y_line -= 1
        print(f"Марсоход находится на позиции {x_line}, {y_line}, введите команду:")
    elif (x_line > 1) and (operators_move == "a"):
        x_line -= 1
        print(f"Марсоход находится на позиции {x_line}, {y_line}, введите команду:")
    elif (x_line < 15) and (operators_move == "d"):
        x_line += 1
        print(f"Марсоход находится на позиции {x_line}, {y_line}, введите команду:")
