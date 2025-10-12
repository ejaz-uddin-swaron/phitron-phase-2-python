prediction = input().split()
a = 0
b = 0

for p in prediction:
    if p == "A":
        a += 1
    else:
        b += 1

total = a + b

a_percentage = (a / total) * 100
b_percentage = (b / total) * 100

if a_percentage > 70 or b_percentage > 70:
    print("Biased Model")
else:
    print("Fair Model")