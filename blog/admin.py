from django.contrib import admin
from .models import Tag, Blog, BlogComment, News, Gallery, Pastime

admin.site.register(Tag)
admin.site.register(Blog)
admin.site.register(BlogComment)
admin.site.register(News)
admin.site.register(Gallery)
admin.site.register(Pastime)

