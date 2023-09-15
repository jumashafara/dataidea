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
    slug = models.CharField(max_length=122, default='New Blog Slug')
    cuid = models.CharField(max_length=122, default='New Cuid')
    title = models.CharField(max_length=122)
    brief = models.TextField(default='')
    cover_image = models.CharField(max_length=122, default='no image')
    popularity = models.FloatField(default=0)
    date_featured = models.CharField(max_length=122, default='no date', null=True)
    content_markdown = models.TextField(default='')

    def __str__(self):
        return self.title
    
    
class BlogComment(models.Model):
    approved = models.BooleanField(default=False) 
    comment = models.TextField(default='New Comment')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, default=12)
    blog = models.ForeignKey(to=Blog, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.comment