from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields.files import ImageField


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to="profiles/%Y", default = "default.jpg")
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
