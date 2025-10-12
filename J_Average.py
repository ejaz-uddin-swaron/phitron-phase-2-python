from functools import reduce

useless = input()
nums = input().split()

nums = list(map(lambda x : float(x), nums))

sum = reduce(lambda x, y : x + y, nums)

ans = sum / len(nums)

print(f"{ans:.7f}")