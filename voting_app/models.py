from django.db import models

# Create your models here.
class Data(models.Model):
    name=models.CharField(max_length=30)
    adhar_id=models.IntegerField()
    voter_id=models.SlugField(max_length=10)
    vote=models.CharField(max_length=30)
    
    
    def __str__(self):
        return self.name