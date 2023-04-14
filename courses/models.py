from django.db import models
from tinymce.models import HTMLField


class Course(models.Model):

    title = models.CharField(
        'заголовок',
        max_length=150,
    )

    text = HTMLField(
        verbose_name='описание',
        help_text='введите ваше описание поста',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
