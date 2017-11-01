from django.db import models
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=50, verbose_name='Оглавление')
    text = models.TextField(max_length=4000, verbose_name='Текст')
    created_date = models.DateTimeField( default=timezone.now, verbose_name='Дата написания статьи')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
