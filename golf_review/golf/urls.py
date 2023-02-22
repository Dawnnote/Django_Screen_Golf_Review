from django.urls import path
from . import views


urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    path("reviews/<int:review_id>/",views.ReviewDetailView.as_view(), name='review-detail'),
    path("reviews/new/", views.ReviewCreateView.as_view(), name="review-create"),
    path("reviews/<int:review_id>/edit/", views.ReviewUpdateView.as_view(), name="review-update"),
    path("reviews/<int:review_id>/delete/", views.ReviewDeleteView.as_view(), name="review-delete"),
]
