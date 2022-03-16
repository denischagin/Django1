import datetime
from django.db import models

from django.utils import timezone

# Create your models here.
class Firstapp(models.Model):
    simple_title = models.CharField('Название статьи', max_length=200)
    simple_text = models.TextField('текст статьи')
    pub_date = models.DateTimeField('дата публикации')
    def __str__(self):
        return self.simple_title
    def was_published(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Comment(models.Model):
    firstapp = models.ForeignKey(Firstapp, on_delete=models.CASCADE)
    name_author = models.CharField('Имя автора комментария', max_length=50)
    text_comment = models.CharField('Текст комментария', max_length=200)

    def __str__(self):
        return self.name_author

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

