from django.shortcuts import render
from django.urls import reverse
from django.views.generic import (
    ListView, DetailView, 
    CreateView, UpdateView,
    DeleteView,
    )
from allauth.account.views import PasswordChangeView
from .models import Review
from .forms import ReviewForm


# Create your views here.
class IndexView(ListView):
    model = Review
    template_name = "golf/index.html"
    context_object_name = "reviews"
    # paginate_by = 4
    # ordering = ["-dt_created"]


class ReviewDetailView(DetailView):
    model = Review
    template_name = "golf/review_detail.html"
    pk_url_kwarg = "review_id"


class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "golf/review_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("review-detail", kwargs={"review_id":self.object.id})


class ReviewUpdateView(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = "golf/review_form.html"
    pk_url_kwarg = "review_id"

    def get_success_url(self):
        return reverse("review-detail", kwargs={"review_id":self.object.id})


class ReviewDeleteView(DeleteView):
    model = Review
    template_name = "golf/review_confirm_delete.html"
    pk_url_kwarg = "review_id"

    def get_success_url(self):
        return reverse("index")


class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse('index')

