N = int(input())

X = input().split()

even = 0
odd = 0
positive = 0
negative = 0

for num in X:
    num = int(num)
    if num < 0:
        
        negative += 1
        
        if abs(num) % 2 == 0:
            even += 1
        else:
            odd += 1

    elif num > 0:
        
        positive += 1
        
        if abs(num) % 2 == 0:
            even += 1
        else:
            odd += 1
    else:
        even += 1

print(f"Even: {even}")   
print(f"Odd: {odd}")   
print(f"Positive: {positive}")   
print(f"Negative: {negative}")   