from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from .utils import get_timestamp_path


class Author(models.Model):
    """Model definition for Author."""

    author = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.author    


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, unique=True, verbose_name='Название')
    order = models.SmallIntegerField(default=0, db_index=True, verbose_name='Порядок')


class New(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    rubric = models.ForeignKey(Rubric, on_delete=models.PROTECT, verbose_name='Рубрика')
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')
    image = models.ImageField(blank=True, upload_to=get_timestamp_path, verbose_name='Изображение')
    content = models.TextField(verbose_name='Содержание')
    is_active = models.BooleanField(default=True, db_index=True, verbose_name='Выводить в списке?')
    publish = models.DateTimeField(default=timezone.now())
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def delete(self, *args, **kwargs):
        for ai in self.additionalimage_set.all():
            ai.delete()
        super(New, self).delete(*args, **kwargs)
    
    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


class AdditionalImage(models.Model):
    new = models.ForeignKey(New, on_delete=models.CASCADE, verbose_name='Новость')
    image = models.ImageField(upload_to=get_timestamp_path, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Дополнительная иллюстрация'
        verbose_name_plural = 'Дополнительные иллюстрации'


class Comment(models.Model):
    new = models.ForeignKey(New, on_delete=models.CASCADE, verbose_name='Новость')
    commentator = models.CharField(max_length=30, verbose_name='Комментатор')
    content = models.TextField(verbose_name='Содержание')
    is_active = models.BooleanField(default=True, db_index=True, verbose_name='Выводить на экран?')
    created = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликован')

    class Meta:
        ordering = ['created']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


# def post_save_dispatcher(sender, **kwargs):
#     author = kwargs['instance'].ak.author
#     if kwargs['created'] and author.send_messages:
#         send_new_comment_notification(kwargs['instance'])

# post_save.connect(post_save_dispatcher, sender=Comment)
