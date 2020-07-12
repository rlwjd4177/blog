from django import forms
from .models import *

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','body','image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']