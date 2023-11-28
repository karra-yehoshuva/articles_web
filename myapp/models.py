# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=100,blank=True,null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    likes = models.ManyToManyField(User,related_name='likes')
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('Artical_detail',args=[self.id,self.slug])
    
    def total_likes(self):
        return self.likes.count()
    

@receiver(pre_save,sender = Article)
def slug_pre_save(sender,**kwargs):
    slug1 = slugify(kwargs['instance'].title)
    kwargs['instance'].slug = slug1
        

#jashu -->abcd
#shalem -->abcd123
#rajesh -->abcd4321