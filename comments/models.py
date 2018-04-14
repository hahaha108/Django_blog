from django.db import models
from user.models import User
from blog.models import Post

# Create your models here.

class Comment(models.Model):
    author = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    created_time = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:20]