from django import forms
from .models import User, Review, Comment, UserComment


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "title",
            "golf_name",
            "golf_link",
            "rating",
            "image1",
            "image2",
            "image3",
            "content",
        ]
        widgets = {
            "rating": forms.RadioSelect
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "nickname",
            "profile_pic",
            "intro",
        ]
        widgets = {
            "intro": forms.Textarea,
        }

class UserCommentForm(forms.ModelForm):
    class Meta:
        model = UserComment
        fields = [
            'content',
        ]
        widgets = {
            'content': forms.Textarea,
        }





class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)