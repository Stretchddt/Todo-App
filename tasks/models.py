from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=400)

    def __str__(self):
        return self.title

class Task(models.Model):
    title = models.CharField(max_length=400)
    category = models.ForeignKey(Category, blank=True, null=True, default=None, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)


    def __str__(self):
        return self.title