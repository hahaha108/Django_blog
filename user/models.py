from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    nickname = models.CharField(
        max_length=128,null=False,blank=False,unique=True,verbose_name='昵称'
    )
    icon = models.ImageField(upload_to='avatar/%Y/%m/%d/', default='default.jpg', null=True,blank=True, verbose_name='头像')

    class Meta(AbstractUser.Meta):
        pass