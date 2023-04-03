start = 1
finish = 101
while True:
  number = (start + finish) // 2
  print('Загаданное число равно, болльше или меньше', number)
  defining_number = int(input('Введите 1, 2 или 3 (1 — равно, 2 — больше, 3 — меньше.)'))
  if defining_number == 2:
    start = number
  elif defining_number == 3:
    finish = number
  else:
    print('Угадал')
    break
