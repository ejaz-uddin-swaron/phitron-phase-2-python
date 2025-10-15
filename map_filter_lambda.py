"""
Problem 4: Square of Even Numbers (Map + Filter + Lambda)
Problem:
 Write a one-line Python expression using map(), filter(), and lambda that takes a list of integers and returns the squares of even numbers only.
Example Input:
nums = [1, 2, 3, 4, 5, 6]

Expected Output:
[4, 16, 36]

"""
nums = [1, 2, 3, 4, 5, 6]

ans = list(map(lambda x : x**2, filter(lambda x : x%2 == 0, nums)))

print(ans)
