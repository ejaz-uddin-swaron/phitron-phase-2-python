T = int(input())

while T != 0:
    N = input()
    N = reversed(N)
    for digits in N:
        print(digits, end=" ")
    print()
    T -= 1

    
