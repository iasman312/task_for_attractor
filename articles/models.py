from django.contrib.auth import get_user_model
from django.db import models


class Article(models.Model):
    category = models.ForeignKey(
        'categories.Category',
        on_delete=models.CASCADE,
        related_name='articles',
        verbose_name='Категория',
        null=False,
        blank=False
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='user_articles',
        verbose_name='Пользователь',
        null=True,
        blank=True
    )
    title = models.CharField(
        max_length=120,
        null=False,
        blank=False,
        verbose_name='Название'
    )
    description = models.TextField(
        max_length=3000,
        null=True,
        blank=True,
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='images',
        null=True,
        blank=True,
        verbose_name='Картинка'
    )

    class Meta:
        db_table = 'articles'
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title
