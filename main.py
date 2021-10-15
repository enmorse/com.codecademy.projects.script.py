last_semester_grade_book = [
    ["politics", 80],
    ["latin", 96],
    ["dance", 97],
    ["architecture", 65],
]

# Your code below:
subjects = [
    "physics",
    "calculus",
    "poetry",
    "history",
]
grades = [
    98,
    97,
    85,
    88,
]

grade_book = [
    ["physics", 98],
    ["calculus", 97],
    ["poetry", 85],
    ["history", 88],
    ["computer science", 100],
    ["visual arts", 93],
]

# print(grade_book)

# print(grade_book)

# print(grade_book)

grade_book[5][1] = 98

# print(grade_book)

grade_book[2].remove(85)

# print(grade_book)

grade_book[2].append("Pass")

# print(grade_book)

full_grade_book = last_semester_grade_book + \
                 grade_book

print(full_grade_book)
