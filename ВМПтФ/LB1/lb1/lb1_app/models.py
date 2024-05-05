from django.db import models

class Student(models.Model):

    name = models.CharField(max_length=100)

    group = models.CharField(max_length=10)

    subject1_marks = models.IntegerField()

    subject2_marks = models.IntegerField()

    subject3_marks = models.IntegerField()


    def __str__(self):

        return self.name