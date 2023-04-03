boys = int(input("Amount of sigma males: "))
girls = int(input("Amountof girls:"))
answer = ""


if (boys > 2 * girls) or (girls > 2 * boys):
    print("Solution does not exist.")
elif boys >= girls:
    koeficient = boys - girls
    for bgb in range(koeficient):
        answer += "BGB"
    for bg in range(girls - koeficient):
        answer += "BG"
else:
    koeficient = girls - boys
    for gbg in range(koeficient):
        answer += "GBG"
    for gb in range(boys - koeficient):
        answer += "GB"

        
print(answer)
