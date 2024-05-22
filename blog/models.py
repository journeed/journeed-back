from django.db import models
from services.mixin import DateMixin, SlugMixin
from django.contrib.auth import get_user_model
from services.slugify import unique_slug_generator

User = get_user_model()


class Blog(DateMixin, SlugMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=350)
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator(self)
        super().save(*args, **kwargs)


class BlogComment(DateMixin):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f'{self.blog} --- {self.user}'
