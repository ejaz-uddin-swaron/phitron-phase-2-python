s = input()
ans = {}

for x in s:
    ans[x] = ans.get(x,0) + 1

ans = {key : ans[key] for key in sorted(ans)}
    
for key, val in ans.items():
    print(f"{key} : {val}")
