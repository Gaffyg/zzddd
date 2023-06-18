from django.db import models
from django.urls import reverse


class Concert(models.Model):
    city = models.CharField('Город концерта', max_length=255)
    place = models.CharField('Место концерта', max_length=255)
    price = models.IntegerField('Цена билета', default=0)
    date = models.DateTimeField('Дата концерта')
    count = models.IntegerField('Кол-во билетов', default=0)
    slug = models.SlugField('URL', unique=True, max_length=100, db_index=True)

    class Meta:
        verbose_name = 'Концерты'
        verbose_name_plural = 'Концерты'

    def __str__(self):
        return f'{self.city}, {self.place}, {self.price}'

    def get_buy_url(self):
        return reverse('buy', kwargs={'concert_slug': self.slug})


class Links(models.Model):
    platform = models.CharField('Платформа', max_length=255)
    link = models.URLField('Ссылка')

    class Meta:
        verbose_name = 'Ссылки'
        verbose_name_plural = 'Ссылки'

    def __str__(self):
        return self.platform


class Clips(models.Model):
    image = models.URLField('Сылка на превью')
    link = models.CharField('Сылка на видео', max_length=300, unique=True)

    class Meta:
        verbose_name = 'Клипы'
        verbose_name_plural = 'Клипы'

    def __str__(self):
        return f'Клип {self.pk}'


class Group(models.Model):
    text = models.TextField(max_length=5000, verbose_name='О группе')
    image = models.ImageField(verbose_name='Фото')

    class Meta:
        verbose_name = 'О группе'
        verbose_name_plural = 'О группе'

    def __str__(self):
        return f'О Группе'


class Buyer(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИО')
    email = models.EmailField(verbose_name='Ваш Email')
    count_bilet = models.IntegerField(verbose_name='Кол-во билетов')
    data_time_buy = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время покупки')
    city = models.CharField(max_length=100, verbose_name='Город')
    place = models.CharField(max_length=100, verbose_name='Место')
    price = models.IntegerField('Цена билета', default=0)

    class Meta:
        verbose_name = 'Покупателя'
        verbose_name_plural = 'Покупатели'

    def __str__(self):
        return self.name


class News(models.Model):
    post_id = models.IntegerField()
    text = models.CharField(max_length=5000, verbose_name='Текст поста')
    image = models.CharField(max_length=5000, verbose_name='Фото поста')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ('id',)

    def __str__(self):
        return self.text[:10]
