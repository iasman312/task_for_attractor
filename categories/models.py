from django.db import models


class Category(models.Model):
    title = models.CharField(
        max_length=120,
        null=False,
        blank=False,
        verbose_name='Название')

    class Meta:
        db_table = 'categories'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

