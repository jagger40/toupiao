from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User)
    photo = models.FilePathField()
    email = models.EmailField()
    

class Poll(models.Model):
    user = models.ForeignKey(User)
    question = models.CharField(max_length=200)
    story = models.TextField(max_length=3000)
    keyword = models.CharField(max_length=20)
    visted = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    
    def __unicode__(self):
        return self.question

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __unicode__(self):
        return self.choice


class Comment(models.Model):
    poll = models.ForeignKey(Poll)
    user = models.ForeignKey(User)
    pub_date = models.DateTimeField('date comment')
    text = models.TextField(max_length=200)
    def __unicode__(self):
        return self.text