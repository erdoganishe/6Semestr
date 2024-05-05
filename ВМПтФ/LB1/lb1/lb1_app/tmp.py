import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '../lb1/settings')

import django
django.setup()

from lb1_app.models import Student

students = [
    Student(name='John Doe', group='A', subject1_marks=85, subject2_marks=90, subject3_marks=80),
    Student(name='Jane Doe', group='B', subject1_marks=95, subject2_marks=85, subject3_marks=92),
    Student(name='Bob Smith', group='A', subject1_marks=75, subject2_marks=80, subject3_marks=85),
]

for student in students:
    student.save()