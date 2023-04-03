name, borrowed = input("Write name and amount"
                       "of money that should be returned:").split()

while True:
    print(f"Hi,{name}, you need to return {borrowed} in cash.\nHow much will "
      "you return now? ", end="")

    money = int(input())

    if money < int(borrowed):
        print("It's not enough")
    else:
        print("Super")
        break
