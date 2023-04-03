start = int(input("Start of segment: "))
finish = int(input("Finish of segment: "))
step = int(input("Step for row: "))


if step < 1:
    step = step * -1
    


if start > finish:
    temperary_variable = start
    start = finish
    finish = temperary_variable


for x in range(start, finish, step):
    y = x ** 3 + 2 * x ** 2 - 4 * x + 1
    print(y)

