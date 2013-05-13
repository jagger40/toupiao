# -*- coding: utf-8 -*-  
from django.db import models
from django.contrib.auth.models import User
from auth.models import Account
    
class Poll(models.Model):
    account = models.ForeignKey(Account)
    question = models.CharField(max_length=200)
    story = models.TextField(max_length=3000)
    keyword = models.CharField(max_length=20)
    visted = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.question

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    nm_votes = models.IntegerField(default=0)
    def __unicode__(self):
        return self.choice


class Comment(models.Model):
    poll = models.ForeignKey(Poll)
    account = models.ForeignKey(Account)
    pub_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=200)
    def __unicode__(self):
        return self.text