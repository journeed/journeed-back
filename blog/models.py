from django.db import models
from services.mixin import DateMixin, SlugMixin
from django.contrib.auth import get_user_model
from services.slugify import unique_slug_generator
from services.uploader import Uploader

User = get_user_model()


class Tag(DateMixin):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Blog(DateMixin, SlugMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=Uploader.blog_image_uploader)
    title = models.CharField(max_length=350)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator(self, slug_name=self.title)
        super().save(*args, **kwargs)


class BlogComment(DateMixin):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f'{self.blog} --- {self.user}'


class News(DateMixin, SlugMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=Uploader.advice_image_uploader)
    title = models.CharField(max_length=350)
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "News"
        verbose_name_plural = "News"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator(self)
        super().save(*args, **kwargs)


class Gallery(DateMixin):
    image = models.ImageField(upload_to=Uploader.gallery_image_uploader)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"


class Pastime(DateMixin):
    image = models.ImageField(upload_to=Uploader.pastime_photo_uploader)
    title = models.CharField(max_length=350)
    content = models.TextField()

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Pastime"
        verbose_name_plural = "Pastimes"


