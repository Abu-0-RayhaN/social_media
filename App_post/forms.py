from django import forms
from django.db.models import fields
from .models import Posts

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields =['image','caption']
        