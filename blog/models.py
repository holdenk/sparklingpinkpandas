from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField
from urllib import request
# Create your models here.




class Rply(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)     
    reply_text = models.TextField(default=None)
    #like_count = models.IntegerField(default=0)
    created_on = models.DateTimeField(default=timezone.now)

class Coment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1) 
    comment_text = models.TextField()
    #like_count = models.IntegerField(default=0)
    rplies = models.ManyToManyField(Rply,related_name='replies',default=None)
    created_on = models.DateTimeField(auto_now_add=True)



class Post(models.Model):
    title = models.CharField(max_length=100,default=None)
    description = RichTextField()
    date_posted = models.DateTimeField(default=timezone.now)
    like_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='img/article/',default=0)
    coments = models.ManyToManyField(Coment,related_name='commentss',blank=True)
    comment_count = models.IntegerField(default=0)
    liker = models.ManyToManyField(User,default=None,blank=True,related_name='liker')


    def get_absolute_url(self):
        return reverse('article', args=(str(self.id)))