from django.db import models
from services.mixin import DateMixin, SlugMixin
from services.uploader import Uploader
from django.contrib.auth import get_user_model

Users = get_user_model()


class Story(DateMixin):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    file = models.FileField(upload_to=Uploader.story_uploader)
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.full_name

    class Meta:
        ordering = ('-created_at', )
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'


class StoryComment(DateMixin):
    story = models.ForeignKey(Story, models.CASCADE)
    user = models.ForeignKey(Users, models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return self.user.full_name

    class Meta:
        ordering = ('-created_at', )
        verbose_name = 'Story Comment'
        verbose_name_plural = 'Story Comments'


class StoryLike(DateMixin):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.story.user} --- {self.user.full_name}'


class StoryCommentLike(DateMixin):
    story_comment = models.ForeignKey(StoryComment, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.story_comment} --- {self.user.full_name}'

