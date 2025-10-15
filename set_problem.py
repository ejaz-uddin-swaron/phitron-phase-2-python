"""
Problem 1: Common Friends (Set Operations)
Problem:
 Given two sets of friends from two people, find the mutual friends, unique friends of each, and the total number of unique friends.
Example Input:
a_friends = {"Rahim", "Karim", "Sakib", "Jamal"}
b_friends = {"Sakib", "Jamal", "Rafiq", "Nadim"}

Expected Output:
Mutual friends: {'Sakib', 'Jamal'}
Unique to A: {'Rahim', 'Karim'}
Unique to B: {'Rafiq', 'Nadim'}
Total unique friends: 6

"""

a_friends = {"Rahim", "Karim", "Sakib", "Jamal"}
b_friends = {"Sakib", "Jamal", "Rafiq", "Nadim"}

# mutual_friends = a_friends & b_friends
mutual_friends = a_friends.intersection(b_friends)
print(f"Mutual friends: {mutual_friends}")

a_unique_friends = a_friends - b_friends
print(f"Unique friends of a: {a_unique_friends}")

b_unique_friends = b_friends - a_friends
print(f"Unique friends of b: {b_unique_friends}")

for x in b_friends:
    a_friends.add(x)

print(f"Total unique friends: {len(a_friends)}")
