timetable = {
    "Day 1": ["Math", "Science", "English", "SS", "Hindi", "Gujarati"],
    "Day 2": ["Science", "Math", "SS", "English", "Gujarati", "Hindi"],
    "Day 3": ["English", "SS", "Math", "Science", "Hindi", "Gujarati"],
    "Day 4": ["SS", "English", "Science", "Math", "Gujarati", "Hindi"],
    "Day 5": ["Math", "English", "Science", "SS", "Hindi", "Gujarati"],
    "Day 6": ["Science", "SS", "Math", "English", "Gujarati", "Hindi"]
}

teachers = {
    "Science": "Vivek",
    "English": "Priya",
    "SS": "Manish",
    "Math": "Aditya",
    "Gujarati": "Meetlesh",
    "Hindi": "neha"
}

for day, subjects in timetable.items():
    print(f"\n{day}")
    print("-" * 20)
    for subject in subjects:
        print(f"{subject} -> {teachers.get(subject, 'No Teacher')}")