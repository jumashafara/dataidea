from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=122)
    image = models.ImageField(upload_to='services', default='services/service.html')
    description = models.TextField(default="One of our services")

    def __str__(self):
        return self.name

class Feature(models.Model):
    FEATURE_IMAGES = []
    name = models.CharField(max_length=122)
    image = models.CharField(max_length=1, choices=FEATURE_IMAGES)
    description = models.TextField()

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=122)
    position = models.CharField(max_length=122)
    testimony = models.TextField()

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    CATEGORIES = [('web', 'Web'), ('other', 'Other'), ('tutorial', 'Tutorial')]      
    name = models.CharField(max_length=122)
    image = models.ImageField(upload_to='portfolio')
    category = models.CharField(max_length=8, choices=CATEGORIES)
    client = models.CharField(max_length=50, default='Private')
    url = models.CharField(max_length=100, default='No url')
    date = models.DateField(null=True)
    description = models.TextField(default='No description')

    def __str__(self):
        return self.name
    

class Price(models.Model):
    name = models.CharField(max_length=122)
    price = models.CharField(max_length=122)
    service = models.ForeignKey(to=Service, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class FrequentlyAskedQuestion(models.Model):
    question = models.CharField(max_length=122)
    answer = models.TextField()

    def __str__(self):
        return self.question

class Contact(models.Model):
    CONTACT_IMAGES = []
    name = models.CharField(max_length=122)
    image = models.CharField(max_length=1, choices=CONTACT_IMAGES)
    contact = models.CharField(max_length=122)

    def __str__(self):
        return self.name
    

