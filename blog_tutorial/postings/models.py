from django.db import models
from django.conf import settings
from django.urls import reverse
from rest_framework.reverse import reverse as api_reverse
# Create your models here.
from django.contrib.auth.models import User

class BlogPost(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=120,null=True,blank=True)
    content = models.CharField(max_length=120,null=True,blank=True)
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)




    @property
    def owner(self):
        return self.user

    def get_api_url(self,request = None):
        return api_reverse("api-postings:post-rud",kwargs={'pk':    self.pk},request=request)

