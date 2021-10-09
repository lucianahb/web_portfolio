from django.db import models
from django.conf import settings
from django.utils import timezone


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class PostArticle(TimeStampMixin):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False, blank=False)
    article = models.TextField(null=False, blank=False)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
