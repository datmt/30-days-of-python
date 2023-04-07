# Creating a dictionary of student grades
grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Dave": 90
}

print("Bob's grade is: " + str(grades["Bob"]))

print("Keys:")
print(grades.keys())

print("Values:")
print(grades.values())

print("Dictionary Items:")
print(grades.values())
for item in grades.items():
    print(item)
