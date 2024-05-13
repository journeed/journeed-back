from django.contrib import admin
from .models import Story, StoryComment, StoryLike, StoryCommentLike

admin.site.register(Story)
admin.site.register(StoryComment)
admin.site.register(StoryLike)
admin.site.register(StoryCommentLike)
