from django.contrib import admin
from .models import Post, Material, Video, Section
# Register your models here.
admin.site.register(Post)
admin.site.register(Section)
admin.site.register(Material)
admin.site.register(Video)