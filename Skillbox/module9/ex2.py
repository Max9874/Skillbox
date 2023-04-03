index = 0
message = input("Type message: ")
remade_message = ""

for symbol in message:
    
    if index == 2:
        remade_message += "*"  
        
    remade_message += symbol

    index += 1

print(remade_message)
