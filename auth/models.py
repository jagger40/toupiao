from django.db import models
import hashlib

# Create your models here.
class Account(models.Model):
    
    email = models.EmailField()
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=20)
    is_active = models.BooleanField()
    avatar = models.ImageField(upload_to='avatar',null=True)
    
    def is_authenticated(self):  
        return True  
    
    def hashed_password(self, password=None):  
        if not password:  
            return self.password  
        else:  
            return hashlib.md5(password).hexdigest() 
        
    def check_password(self, password):  
        if self.hashed_password(password) == self.password:  
            return True  
        return False  
    
    def __unicode__(self):
        return self.email