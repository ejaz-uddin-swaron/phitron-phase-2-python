N = input()
A = input().split()

for i,num in enumerate(A):
    A[i] = int(num)

big = max(A)
small = min(A)

for i,num in enumerate(A):
    if num == big:
        A[i] = small
    elif num == small:
        A[i] = big

print(*A)