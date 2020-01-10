from django.contrib import admin

# Register your models here.
from .models import Post

class PostLlistat(admin.ModelAdmin):
    list_display = ("author", "published_date", "title")

admin.site.register(Post, PostLlistat)
