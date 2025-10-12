inp = input().split()
norm = (float(inp[0]) - float(inp[1])) / (float(inp[2]) - float(inp[1]))
print(f"{norm:.2f}")