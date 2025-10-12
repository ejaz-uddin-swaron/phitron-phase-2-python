rng = int(input())

x = 1
c = 0

for i in range(rng):
    for j in range(x):
        print(chr(c), end="")
    c += 1
    x += 1
    print()

    