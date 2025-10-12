S = input().split()

kw = ["ai", "data", "model", "learn", "train", "neural"]

founded = [word for word in S if word in kw]

if len(founded) >= 2:
    print("AI Detected")
else:
    print("Not AI Related")