def checking(text):
    counter = 0
    remade_text = ""
    for symbol in text:
        counter +=1
        if counter > 10:
            break
        remade_text += symbol
    return remade_text


text = checking(input("Введите 10 букв соответствующие состояниям стоил: "))
counter = 0
daily_milk_producing = 0

for letter in text:
    counter += 1
    if letter == "b":
        daily_milk_producing += counter * 2
        
print(daily_milk_producing)
