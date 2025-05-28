from django.db import models

# Create your models here.

class Person(models.Model):
    name_person = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    available = models.CharField(max_length=40)
    about_me_one = models.TextField()
    about_me_two = models.TextField()

    def __str__(self):
        return self.name_person
    

class Form(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=40)
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name
    
class TechnologiesList(models.Model):
    Technology_name = models.CharField(max_length=16)

    def __str__(self):
        return self.Technology_name
    
class Project(models.Model):
    title = models.CharField()
    description = models.TextField()
    technologies = models.ManyToManyField(TechnologiesList, related_name='projects')
    end_update = models.DateField()
    view_code = models.CharField()

    def __str__(self):
        return self.title







