from django.db import models
from django.utils import timezone
# Create your models here.
class Event(models.Model):
    caption = models.CharField(max_length=100,default=None)
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='img/article/',default=0)
    
    
        