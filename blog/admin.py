from django.contrib import admin

#from django.contrib.auth.models import User, Group

from .models import Post

admin.site.register(Post)
