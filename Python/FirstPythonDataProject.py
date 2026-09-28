# ---------- PROBLEM ----------
# Build a "Student Learning Profile" that captures a student's basic info, the topics we are learning, their location, 
# structured details, their unique skills, and their pending tasks — using the different Python data structures 
# learned so far (variables, string, list, tuple, dictionary, set, and queue).

# Variable - string, int, etc
student_name = "Pallavi Saxena"
current_batch = "AI Architect Engineering"
learning_hours_per_week = 14 # 2 hours/day
is_actively_learning = True

# List
learning_topics = ['Python', 'Linear Algebra', 'Calculas', 'Statistics', 'ML', 'DL', 'NLP', 'CV', 'Gen AI', 'AWS', 'LLops']

# Tuple
location = ("Pune", "Maharashtra", 'India')

# Dictionary
student_details = {
    "name": "Pallavi Saxena",
    "Current_rol": "AI/ ML Lead",
    "goal": "AI Architecture"
}

# Set
unique_skills = ("Python", 'NLP', 'RAG', 'LLM', 'Communication')

# Queue
from collections import deque
task_queue = deque(["Revise Data Structure", "Complete Assignment", "Complete Mini Project"])

# ---------- EXECUTION / OUTPUT ----------
print("---- Variables ----")
print(student_name)
print(current_batch)
print(learning_hours_per_week)
print(is_actively_learning)
print()

print("---- List (Learning Topics) ----")
print(learning_topics)
print()

print("---- Tuple (Location) ----")
print(location)
print()

print("---- Dictionary (Student Details) ----")
print(student_details)
print()

print("---- Set (Unique Skills) ----")
print(unique_skills)
print()

print("---- Queue (Task Queue) ----")
print(task_queue)
