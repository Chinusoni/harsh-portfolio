from django.db import models

class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.CharField(max_length=50) # e.g., "Jan 2023"
    end_date = models.CharField(max_length=50)   # e.g., "Present"
    description = models.TextField()

    def __str__(self):
        return f"{self.title} at {self.company}"