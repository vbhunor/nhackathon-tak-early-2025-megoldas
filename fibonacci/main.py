with open('./input.txt', 'r') as f:
    input = f.read().split()
    lista = input

for i in lista:
    try:
        n = int(i)
        fi_old1 = 0
        fi_old2 = 1
        oszthato_3mal = []

        for _ in range(n):
            fi_new = fi_old1 + fi_old2
            if fi_new % 3 == 0:
                oszthato_3mal.append(str(fi_new))
            fi_old1 = fi_old2
            fi_old2 = fi_new

        print(", ".join(oszthato_3mal) if oszthato_3mal else "N/A")
    except ValueError:
        print("N/A")

print("Bemenet:", input)
