# student_info.py
# A small program that stores a student's details in a dictionary
# and prints them in a neat, readable format.


def create_student(name, batch, course, learning_goal, skills):
    """Build and return a dictionary holding one student's details."""
    # A dictionary stores data as "key: value" pairs
    student = {
        "Name": name,
        "Batch": batch,
        "Course": course,
        "Learning Goal": learning_goal,
        "Skills": skills,  # a value can also be a list
    }
    return student


def print_student_info(student):
    """Print the student's details neatly, one per line."""
    # Find the longest key so all the values line up in a column
    width = max(len(key) for key in student)

    print("=" * 40)
    print("STUDENT INFORMATION".center(40))
    print("=" * 40)

    # .items() gives us each key and its value together
    for key, value in student.items():
        # If the value is a list, join its items into one string
        # e.g. ["Python", "Git"] becomes "Python, Git"
        if isinstance(value, list):
            value = ", ".join(value)

        # ljust(width) pads the key with spaces so the colons line up
        print(f"{key.ljust(width)} : {value}")

    print("=" * 40)


def main():
    """Starting point of the program."""
    # Change these values to your own details
    student = create_student(
        name="Pallavi Saxena",
        batch="2026",
        course="Python Programming",
        learning_goal="Build real projects with Python",
        skills=["Python", "Git", "Problem Solving", "AWS", "ML", "NLP"],
    )
    print_student_info(student)


main()
