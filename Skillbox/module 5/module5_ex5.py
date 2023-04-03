import random

while True:
    input()
    a,b,c = random.randint(1,3), random.randint(1,3), random.randint(1,3)
    if a == b == c:
        print("3")
    elif a == b or a == c or b == c:
        print("2")
    else:
        print("1")
