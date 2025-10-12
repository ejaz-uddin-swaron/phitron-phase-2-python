S = input().split()

# enumerate() did not taught in the class but I know this before
for i,num in enumerate(S):
    S[i] = int(num)

avg = sum(S) / len(S)

if avg < 85: 
    print("Dark Image")
elif avg <= 170: 
    print("Normal Image") 
elif avg > 170:
    print("Bright Image")