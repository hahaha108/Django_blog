from django.db import models
from django.urls import reverse
import markdown
from django.utils.html import strip_tags
from ckeditor.fields import RichTextField

from user.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=60)
    titleimg = models.ImageField(upload_to='titleimg/%Y/%m/%d/',null=True,blank=True)
    body = RichTextField()

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    excerpt = models.CharField(max_length=300,null=True,blank=True)
    category = models.ForeignKey('Category',None)
    tags = models.ManyToManyField('Tag')
    author = models.ForeignKey(User,None)
    views = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('myblog:detail',kwargs={'pk':self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def save(self,*args,**kwargs):
        if not self.excerpt:
            mk = markdown.Markdown(
                extensions=[
                    'markdown.extensions.extra',
                    'markdown.extensions.codehilite',
                    'markdown.extensions.toc'
                ]
            )
            self.excerpt = strip_tags(mk.convert(self.body))[:108]
        super(Post, self).save(*args,**kwargs)
