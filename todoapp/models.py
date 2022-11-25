from django.db import models


# Create your models here.
class TodoListItem(models.Model):
    user = models.CharField(max_length=100)
    content = models.TextField() 