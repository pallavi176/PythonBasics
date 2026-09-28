# Lists

skills = ['Python', 'Git', 'AI', 'SQL', "AWS"]
print(skills)

print(skills[0])
print(skills[1])
print(skills[1:3])
print(skills[-1])

skills[2] = 'AI/ML'
print(skills)

skills[-1] = 3
print(skills)

skills[-1] = 'aws'
print(skills)

skills.append('NLP')
print(skills)

todo = ['Wakeup', 'Fresh up', 'Yoga', 'Go to Office', 'Work']
print(todo)

cart_items = ["Laptop", "Mouse", "Keyboard", "Headphones"]
print(cart_items)


# Tuple:
location = ("Bangalore", 'Karnataka', 'India')
print(location)
print(location[0])

#location[0] = 'Bengaluru'
print(location)

dob = (14, "August", 1998)
print(dob)
print(dob[-1])
color = (255, 99, 71)
print(color)


# Queue
#FIFO: First In First Out

from collections import deque
task_queue = deque(["Task 1", "Task 2", "Task 3"])
print(task_queue)

support_queue = deque(["Ticket#101", "Ticket#102", "Ticket#103", "Ticket#104", "Ticket#105"])
print(support_queue)

print_queue = deque(["Resume.pdf", "Invoice.docx", "Report.pdf"])
print(print_queue)