from django.contrib import admin
from .models import UserInfo, Category, Post

# Register your models here.
admin.site.register(UserInfo)
admin.site.register(Category)
admin.site.register(Post)