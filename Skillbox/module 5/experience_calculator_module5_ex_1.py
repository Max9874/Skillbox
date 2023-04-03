### Счётчик опыта ###

while True:
    experience = int(input("Введите количество опыта:"))

    if experience >= 8500:
        print((experience - 2500) // 5000)
        print("level = {0}".format(3 + ((experience - 2500) // 5000)))
    
    elif experience >= 3500:
        print("level = 3")
    elif experience >= 1000:
        print("level = 2")
    else:
        print("level = 1")
    
