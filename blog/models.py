from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()



# Create your models here.

class Profile(models.Model):
    image = models.ImageField(upload_to="profiles/%Y", default = "default.jpg")
    bio = models.TextField()

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
        

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to="posts/%Y")
    publish_date = models.DateTimeField(auto_now_add = True)
    last_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20)
    slug = models.SlugField(
        verbose_name='slug',
        allow_unicode=True,
        max_length=255,
        help_text=("The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/")
    )
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class Comment(models.Model):
    timestamp = models.DateTimeField(auto_now=False)


class PostView(models.Model):

    timestamp = models.TimeField(auto_now_add=True)


    user = models.ForeignKey(User, on_delete=models.SET_NULL, null =True)
    posts = models.ForeignKey(Post, on_delete=models.CASCADE)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    posts = models.ForeignKey(Post, on_delete=models.SET_NULL,null =True, unique= True)
    
    def __str__(self):
        return self.User.username




