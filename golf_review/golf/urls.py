from django.urls import path
from . import views


urlpatterns = [
    # review
    path("", views.IndexView.as_view(), name='index'),
    # path('reviews/following/', views.FollowingReviewListView.as_view(), name='following-review-list'),
    path("reviews/<int:review_id>/",views.ReviewDetailView.as_view(), name='review-detail'),
    path("reviews/new/", views.ReviewCreateView.as_view(), name="review-create"),
    path("reviews/<int:review_id>/edit/", views.ReviewUpdateView.as_view(), name="review-update"),
    path("reviews/<int:review_id>/delete/", views.ReviewDeleteView.as_view(), name="review-delete"),

    # profile urls
    path("users/<int:user_id>/", views.ProfileView.as_view(), name="profile"),
    path("user/<int:user_id>/reviews/", views.UserReviewListView.as_view(), name="user-review-list"),
    path("set-profile/", views.ProfileSetView.as_view(), name="profile-set"),
    path("edit-profile/", views.ProfileUpdateView.as_view(), name="profile-update"),

    # comment url
    path(
        'reviews/<int:review_id>/comments/create/',
        views.CommentCreateView.as_view(),
        name='comment-create',
    ),
    path(
        'comments/<int:comment_id>/edit/', 
        views.CommentUpdateView.as_view(), 
        name='comment-update'
    ),
    path(
        'comments/<int:comment_id>/delete/', 
        views.CommentDeleteView.as_view(), 
        name='comment-delete'
    ),

    # like url
    path(
        'like/<int:content_type_id>/<int:object_id>/',
        views.ProcessLikeView.as_view(),
        name='process-like'
    ),

    # follow url
    path(
        'users/<int:user_id>/follow/',
        views.ProcessFollowView.as_view(),
        name='process-follow'
    ),
    path('users/<int:user_id>/following/', views.FollowingListView.as_view(), name='following-list'),
    path('users/<int:user_id>/followers/', views.FollowerListView.as_view(), name='follower-list'),



    # other page url
    path("screen/", views.GotoScreenGolf.as_view(), name="go-to-screengolf"),
    path("practice/", views.GotoPracticeGolf.as_view(), name="go-to-practicegolf"),

    path('post/', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail')
]
