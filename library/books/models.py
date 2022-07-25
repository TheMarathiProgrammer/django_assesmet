from pyexpat import model
from django.db import models

# Create your models here.
class Books (models.Model):
    isbn = models.CharField(max_length=15)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    	
    def __str__(self):
	    return (self.title)

