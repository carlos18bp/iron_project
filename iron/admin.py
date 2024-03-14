from django.contrib import admin
from .models.blog import Blog
from .models.user import User

admin.site.register(Blog)
admin.site.register(User)
