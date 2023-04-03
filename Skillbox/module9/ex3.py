kolvo_ryadov = int(input("Kol-vo ryadov: "))
kolvo_sideniy = int(input("Kol-vo sideniy v ryadu: "))
distance = int(input("Дистанция между рядами: "))

for _ in range(kolvo_ryadov):
    print("=" * kolvo_sideniy, "*" * distance, "=" * kolvo_sideniy)
