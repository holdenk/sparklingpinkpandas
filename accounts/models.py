from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class User_Details(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_details')
    image = models.ImageField(upload_to='img/profile/',default='img/profile/default.jpg')
    

class Mailing(models.Model):
    email = models.CharField(max_length=128)