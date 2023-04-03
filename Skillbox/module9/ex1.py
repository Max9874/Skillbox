counter = 0

for _ in range(10):
	user_input = input("Type keyword: ").lower()
	if user_input == "карамба":
		counter += 1

print(counter)
