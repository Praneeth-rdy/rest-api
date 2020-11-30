from django.db import models

# Create your models here.
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


    def __str__(self):
        return self.title