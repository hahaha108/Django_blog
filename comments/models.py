from django.db import models
from user.models import User
from blog.models import Post

# Create your models here.

class Comment(models.Model):
    author = models.ForeignKey(User,on_delete=None)
    created_time = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    post = models.ForeignKey(Post,on_delete=None)

    def __str__(self):
        return self.text[:20]