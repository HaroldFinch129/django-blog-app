from django.contrib import admin
from .models import Comment, Like, PostView, Profile, Category, Post

# Register your models here.

admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostView)
admin.site.register(Comment)
admin.site.register(Like)





