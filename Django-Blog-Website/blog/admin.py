from django.contrib import admin
from .models import Post
# Register your models here.

# Put post object on admin page
admin.site.register(Post)
