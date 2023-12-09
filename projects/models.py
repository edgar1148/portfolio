from django.db import models
from django.urls import reverse


class Projects(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    category = models.CharField(
        max_length=255,
        default="uncategorized",
        verbose_name='Категория'
    )
    slug = models.SlugField(
        max_length=250,
        verbose_name='URL',
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Изображение',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления',
    )

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('projects:projects_detail', args=[str(self.slug)])
