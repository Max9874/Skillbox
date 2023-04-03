N = int(input("N: "))
summary  = 0

for x in range(0, N):
    print(f"{x}: ")
    element_n = (-1)** x * 1 / 2 ** x
    summary += element_n
    print(element_n)
    
print("\n",1 - element_n)
