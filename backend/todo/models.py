from django.db import models

# Create your models here.

# Models


class Todo(models.Model):
    title = models.TextField()
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
