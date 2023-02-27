from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.utils.text import slugify
from .validators import validate_no_special_characters, validate_golf_link
from django.utils import timezone
from embed_video.fields import EmbedVideoField
# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(
        max_length=15,
        unique=True,
        null=True,
        validators = [validate_no_special_characters],
        error_messages={"unique":"이미 사용중인 닉네임입니다"},
    )

    profile_pic = models.ImageField(
        default="default_profile_pic.jpg", upload_to="profile_pics"
    )

    intro = models.CharField(max_length=60, blank=True)
    following = models.ManyToManyField(
        'self', 
        symmetrical=False, 
        blank=True, 
        related_name='followers'
    )

    def __str__(self):
        return self.email


class Review(models.Model):
    title = models.CharField(max_length=30)
    golf_name = models.CharField(max_length=20)
    golf_link = models.URLField(max_length=500, validators=[validate_golf_link])

    RATING_CHOICES = [
        (1, "★"),
        (2, "★★"),
        (3, "★★★"),
        (4, "★★★★"),
        (5, "★★★★★"),
    ]
    rating = models.IntegerField(choices=RATING_CHOICES, default=None)

    image1 = models.ImageField(upload_to="review_pics")
    image2 = models.ImageField(upload_to="review_pics", blank=True)
    image3 = models.ImageField(upload_to="review_pics", blank=True)
    content = models.TextField()
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_updated = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')

    likes = GenericRelation('Like', related_query_name='review')

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-dt_created']



class UserComment(models.Model):
    content = models.TextField(max_length=500, blank=False)
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_updated = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')

    likes = GenericRelation('Like', related_query_name='comment')

    def __str__(self):
        return self.content[:30]
    
    class Meta:
        ordering = ['-dt_created']


class Like(models.Model):
    dt_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    liked_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"({self.user}, {self.liked_object})"
    
    class Meta:
        unique_together = ['user', 'content_type', 'object_id']








class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    header_img = models.ImageField(upload_to='notice/images/%Y/%m/%d/', blank=True)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.text



## Board
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, allow_unicode=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Board(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    video = EmbedVideoField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title