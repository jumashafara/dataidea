from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tutor(models.Model):
    name = models.CharField(max_length=122, default='New Tutor')
    
    def __str__(self):
        return self.name
    
class Organization(models.Model):
    name = models.CharField(max_length=122, default='DataIdea')
    url = models.CharField(max_length=122, default='dataidea.com')

    def __str__(self):
        return self.name

class Course(models.Model):
    LEVELS = [('introductory', 'reception-1')]
    name = models.CharField(max_length=122, default='New Course')
    description = models.TextField(default='New Course')
    organization = models.ForeignKey(to=Organization, default=0, on_delete=models.CASCADE)
    tutors = models.ManyToManyField(to=Tutor, default='Not Identified')
    level = models.CharField(max_length=22, choices=LEVELS, default='reception-1')
    learners = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Learner(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(to=Course)
    subscription_end = models.DateField(null=True)

    def __str__(self):
        return self.user.username




class Video(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=122, default='New Video')
    url = models.CharField(max_length=122, default='New Video')
    def __str__(self):
        return self.name

class Question(models.Model):
    video = models.ForeignKey(to=Video, on_delete=models.CASCADE)
    question = models.CharField(max_length=122, default='New Question')
    answer = models.CharField(max_length=122, default='New Answer')

    def __str__(self):
        return self.question
    

class Quiz(models.Model):
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=122, default='New Quiz')
    questions = models.ManyToManyField(to=Question)

    def __str__(self):
        return self.name
    



