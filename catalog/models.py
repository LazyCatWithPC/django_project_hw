from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('id',)


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='имя')
    description = models.TextField(max_length=500, verbose_name='описание', null=True)
    preview = models.ImageField(verbose_name='изображение (превью)', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за покупку')
    creation_date = models.DateTimeField(verbose_name='дата создания')
    last_change_date = models.DateTimeField(verbose_name='дата последнего изменения', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('id',)


class Blog(models.Model):
    name = models.CharField(max_length=250, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL", **NULLABLE)
    content = models.TextField(verbose_name='Содержимое')
    image = models.ImageField(upload_to='blogs/', verbose_name='Изображение', **NULLABLE)
    creation_at = models.DateField(verbose_name='Дата публикации')
    publication = models.BooleanField(default=True, verbose_name='Признак публикации')
    number_views = models.IntegerField(default=0, verbose_name='Количество просмотров', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
