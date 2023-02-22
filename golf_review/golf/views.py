from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    ListView, DetailView, 
    CreateView, UpdateView,
    DeleteView,
    )
from braces.views import LoginRequiredMixin, UserPassesTestMixin
from allauth.account.models import EmailAddress
from allauth.account.views import PasswordChangeView
from .models import Review, User
from .forms import ReviewForm, ProfileForm
from .functions import confirmation_required_redirect


# Create your views here.
class IndexView(ListView):
    model = Review
    template_name = "golf/index.html"
    context_object_name = "reviews"
    paginate_by = 4
    ordering = ["-dt_created"]


class ReviewDetailView(DetailView):
    model = Review
    template_name = "golf/review_detail.html"
    pk_url_kwarg = "review_id"


class ReviewCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "golf/review_form.html"

    redirect_unauthenticated_users = True
    raise_exception = confirmation_required_redirect

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("review-detail", kwargs={"review_id":self.object.id})

    def test_func(self, user):
        return EmailAddress.objects.filter(user=user, verified=True).exists()


class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = "golf/review_form.html"
    pk_url_kwarg = "review_id"

    raise_exception = True

    def get_success_url(self):
        return reverse("review-detail", kwargs={"review_id":self.object.id})

    def test_func(self, user):
        review = self.get_object()
        return review.author == user


class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    template_name = "golf/review_confirm_delete.html"
    pk_url_kwarg = "review_id"

    raise_exception = True

    def get_success_url(self):
        return reverse("index")

    def test_func(self, user):
        review = self.get_object()
        return review.author == user


class ProfileView(DetailView):
    model = User
    template_name = "golf/profile.html"
    pk_url_kwarg = "user_id"
    context_object_name = "profile_user"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.kwargs.get("user_id")
        context["user_reviews"] = Review.objects.filter(author__id=user_id).order_by("-dt_created")[:4]
        return context

class UserReviewListView(ListView):
    model = Review
    template_name = "golf/user_review_list.html"
    context_object_name = "user_reviews"
    paginate_by = 4

    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        return Review.objects.filter(author__id=user_id).order_by("dt_created")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile_user"] = get_object_or_404(User, id=self.kwargs.get("user_id"))
        return context

    
class ProfileSetView(LoginRequiredMixin,UpdateView):
    model = User
    form_class = ProfileForm
    template_name = "golf/profile_set_form.html"

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse("index")


class ProfileUpdateView(LoginRequiredMixin,UpdateView):
    model = User
    form_class = ProfileForm
    template_name = "golf/profile_update_form.html"

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse("profile", kwargs=({"user_id": self.request.user.id}))


class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    def get_success_url(self):
        return reverse('profile', kwargs={"user_id": self.request.user.id})

