from django.contrib import admin

# Register your models here.
from blog.models import Post # наша модель из blog/models.py

admin.site.register(Post)