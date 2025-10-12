A = input().split()

for i in range(len(A)):
    A[i] = int(A[i])

A.sort()
print(A[0], end=" ")
print(A[2])
