N = int(input())
target = float(input())
loss = []

while N != 0:
    loss.append(float(input()))
    N -= 1

average = sum(loss) / len(loss)

if average <= target:
    print("PASS")
else:
    print("RETRY")
    
