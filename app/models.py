from django.db import models
from django.core.exceptions import ValidationError

# def validate_due_date(value):
#     if value < models.F('timestamp'):
#         raise ValidationError("Due date must be greater than the created date.")

class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Task(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=1000, null=False, blank=False)
    due_date = models.DateField(null=True, blank=True)
    tag = models.ManyToManyField(Tag, null=True, blank=True)

    Choices = (
        ("OPEN", "Open"),
        ("WORKING", "Working"),
        ("DONE", "Done"),
        ("OVERDUE", "Overdue")
    )
    status = models.CharField(max_length=20, choices=Choices, default="OPEN", null=False, blank=False)

    def validate(self, data):
        if data.get('due_date') < data.get('time_stamp'):
            raise ValidationError("Due date must be greater than the created date.")

    def __str__(self):
        return self.title
        