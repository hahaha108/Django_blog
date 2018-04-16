from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from blog.models import Post


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'nickname', 'icon')


class PubilcationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','titleimg','body','category','tags']

# class PubilcationForm(forms.Form):
    # title = forms.CharField(label='标题',max_length=100)
    # body = RichTextFormField(label='正文')

