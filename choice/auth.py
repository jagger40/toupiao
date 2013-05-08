from choice.models import Member

class MyCustomBackend:  
  
    def authenticate(self, email=None, password=None):  
        try:  
            member = Member.objects.get(email=email)  
        except Member.DoesNotExist:  
            pass  
        else:  
            if member.check_password(password):  
                return member  
        return None  
   
    def get_user(self, user_id):  
        try:  
            return Member.objects.get(pk=user_id)  
        except Member.DoesNotExist:  
            return None   
    
    