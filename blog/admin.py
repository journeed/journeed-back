from django.contrib import admin
from .models import Blog, BlogComment, Advice, Gallery, Pastime

admin.site.register(Blog)
admin.site.register(BlogComment)
admin.site.register(Advice)
admin.site.register(Gallery)
admin.site.register(Pastime)

