from django import forms
from .models import User, Review


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["nickname"]

    def signup(self, request, user):
        user.nickname = self.cleaned_data['nickname']
        user.save()

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "title",
            "restaurant_name",
            "restaurant_link",
            "rating",
            "image1",
            "image2",
            "image3",
            "content",
        ]
        widgets = {
            "rating": forms.RadioSelect
        }