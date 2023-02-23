from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Review, Post


# Register your models here.
admin.site.register(User, UserAdmin)
UserAdmin.fieldsets += (("Custom fields", {"fields":("nickname", "profile_pic", "intro")}),)

admin.site.register(Review)
admin.site.register(Post)