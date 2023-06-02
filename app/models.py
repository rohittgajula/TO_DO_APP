from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime

def validate_due_date(value):
        if datetime.combine(value,datetime.min.time()) < datetime.now():
            raise ValidationError("Due date must be greater than the created date.")

class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Task(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=1000, null=False, blank=False)
    due_date = models.DateTimeField(null=True, blank=True, validators=[validate_due_date])
    tag = models.ManyToManyField(Tag, null=True, blank=True)

    Choices = (
        ("OPEN", "Open"),
        ("WORKING", "Working"),
        ("DONE", "Done"),
        ("OVERDUE", "Overdue")
    )
    status = models.CharField(max_length=20, choices=Choices, default="OPEN", null=False, blank=False)


    def __str__(self):
        return self.title
        