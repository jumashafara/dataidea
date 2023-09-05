from django.contrib import admin
from .models import Blog
from .models import Authors
from .models import Hashnode
from .models import BlogComment

# Register your models here.

admin.site.register(model_or_iterable=[Blog, Authors, Hashnode, BlogComment])
