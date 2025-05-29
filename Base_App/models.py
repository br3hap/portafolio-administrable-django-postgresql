from django.db import models

# Create your models here.
class BackendList(models.Model):
    skill_name = models.CharField(max_length=16)

    def __str__(self):
        return self.skill_name
    
class ToolList(models.Model):
    Tool_name = models.CharField(max_length=16)

    def __str__(self):
        return self.Tool_name

class Skill(models.Model):
    skill_backend = models.ManyToManyField(BackendList, related_name='skills_skill')
    tool_backend = models.ManyToManyField(ToolList, related_name='skills_tool')



class Person(models.Model):
    name_person = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    available = models.CharField(max_length=40)
    about_me_one = models.TextField()
    about_me_two = models.TextField()
    about_me_three = models.TextField()
    profession = models.CharField(default='Desarrollador Backend')
    # skill_id = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='people')

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
    

class Page(models.Model):
    title = models.CharField()
    description = models.CharField()
    author = models.CharField()
    name = models.CharField()
    anio = models.DateField()
    rights_reserved = models.CharField()

    def __str__(self):
        return self.name
    







