from django.db import models

# Create your models here.

class Type(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title



class Album(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img/albums')
    Type = models.ForeignKey(Type,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.title