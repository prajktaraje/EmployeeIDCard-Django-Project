from django.db import models

# Create your models here.
class Empid(models.Model):
    name=models.CharField(max_length=122,default='')
    email=models.EmailField(max_length=122,default='')
    post=models.CharField(max_length=122,default='')
    bloodgroup=models.CharField(max_length=122,default='')
    

    def __str__(self):
        return self.name