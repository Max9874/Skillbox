text = input("Type your text here: ") + " "
temperary_counter = 0
longest_word = 0


for symbol in text:
    if symbol == " ":
        if temperary_counter > longest_word:
            longest_word = temperary_counter 
        temperary_counter = 0
        
    else:
        temperary_counter += 1

        
print(longest_word)
