a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
d = 0

counter = 0
summary = 0


if a > b:
    d = a
    a = b
    b = a


for number in range(a, b + 1):
    if number % c == 0:
        summary += number
        counter += 1

print(summary / counter)
