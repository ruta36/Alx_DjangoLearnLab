from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment, Tag
from taggit.forms import TagField


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widgets=TagWidget(),
        required=False
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def clean_tags(self):
        tags = self.cleaned_data['tags']
        if tags:
            tags = [tag.strip() for tag in tags.split(',')]
            tags = [Tag.objects.get_or_create(name=tag)[0] for tag in tags]
        return tags
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        
        
class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']