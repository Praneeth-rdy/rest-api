from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    # [(value, human readable name),....] to create a radio selection field
    user_types = [('user','Normal User'), ('dev','Developer'), ('owner','Owner')]
    user_type = models.CharField(max_length=20, default='user', choices = user_types)

    def __str__(self):
        return self.username


class Employee(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    emp_id = models.IntegerField()

    def __str__(self):
        return self.firstname

class Blog(models.Model):
    title = models.CharField(max_length=100)
    # Image in the blog
    image = models.ImageField(upload_to='blogs')
    body = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="date_published")
    date_updated = models.DateTimeField(auto_now_add=True, verbose_name="date_updated")
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title