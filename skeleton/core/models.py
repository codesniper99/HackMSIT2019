from django.db import models
from django.urls import reverse

# Create your models here.

class ClassificationModel(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text='Enter a name')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name


class RegressionModel(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text='Enter a name')
       
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Dataset(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a name')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name



