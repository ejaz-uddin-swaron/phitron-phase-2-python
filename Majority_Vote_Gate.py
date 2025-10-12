N = int(input())
y = 0
n = 0

while N != 0:  
    S = input()

    if S == "YES":
        y += 1
    else:
        n += 1
    
    N -= 1

if y >= n:
    print("ACCEPT")
else:
    print("REJECT")