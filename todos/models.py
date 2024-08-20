from django.db import models

# Create your models here.
class Todo(models.Model):
    CATEGORY_CHOICES = [
        ('Work', 'Work'),
        ('Personal', 'Personal'),
        ('Shopping', 'Shopping'),
        # Add more categories if needed
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Work')

    def __str__(self):
        return self.title