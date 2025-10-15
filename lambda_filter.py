"""
Problem 3: Word Length Filter (Lambda + Filter)
Problem:
 Given a list of words, use filter() and lambda to return only words whose length is greater than 4.
 Example Input:
words = ["sun", "planet", "moon", "star", "universe"]

Expected Output:
['planet', 'universe']

"""
words = ["sun", "planet", "moon", "star", "universe"]

ans = list(filter(lambda x : len(x) > 4, words))

print(ans)