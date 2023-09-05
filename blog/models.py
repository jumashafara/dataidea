from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Authors(models.Model):
    name = models.CharField(max_length=122, default='dataidea')
    email = models.CharField(max_length=122, default='')
    dateCreated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Blog(models.Model):
    _id = models.CharField(max_length=122, editable=False, unique=True)
    title = models.CharField(max_length=122)
    brief = models.TextField(default='')
    coverImage = models.TextField(default='')
    dateUpdated = models.DateTimeField(auto_now=True)
    dateFeatured = models.DateTimeField(auto_now=True)
    contentMarkdown = models.TextField(default='')
    author = models.ForeignKey(Authors, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
    
class Hashnode(models.Model):
    username = models.CharField(max_length=122)
    blogs_number = models.IntegerField(default=0)
    pages_numeber = models.IntegerField(default=0)

    def __str__(self):
        return self.username
    
class BlogComment(models.Model):
    approved = models.BooleanField(default=False) 
    comment = models.TextField(default='New Comment')
    blog_slug = models.CharField(max_length=122, default='New Blog')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, default=12)
   
    def __str__(self):
        return self.comment