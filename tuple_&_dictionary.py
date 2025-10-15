"""
Problem 2: Sort Students by Marks (Tuple + Dictionary)
Problem:
 You are given a list of tuples — each containing a student's name and mark.
 Sort them in descending order of marks and print the top 3 scorers.
Example Input:
students = [("Rafi", 89), ("Sumi", 95), ("Hasan", 90), ("Nila", 75), ("Anik", 98)]

Expected Output:
Top 3 students:
Anik - 98
Sumi - 95
Hasan - 90

"""

students = [("Rafi", 89), ("Sumi", 95), ("Hasan", 90), ("Nila", 75), ("Anik", 98)]

students = sorted(students, key=lambda x : x[1], reverse=True)

print(f"Top 3 students: ")

for i,x in enumerate(students):
    print(f"{x[0]} - {x[1]}")

    if i >= 2:
        break
    