from django.db import models

# Create your models here.
class Project(models.Model):
    Title = models.CharField(max_length=100)
    Description= models.TextField()
    pub_date = models.DateTimeField()
    author = models.CharField(max_length=50)
   
    
