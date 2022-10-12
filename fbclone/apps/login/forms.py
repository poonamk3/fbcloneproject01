from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User
from django import forms
from .models import Post,Comment
from bootstrap_modal_forms.forms import BSModalModelForm

class SignupForm(UserCreationForm):
	class Meta:
		model=User
		fields=['username','first_name','last_name','email']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','image','description']
        

class CommentFrom(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

