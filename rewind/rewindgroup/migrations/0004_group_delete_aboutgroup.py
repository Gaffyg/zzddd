# Generated by Django 4.1.7 on 2023-03-18 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rewindgroup', '0003_alter_concert_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=5000, verbose_name='О группе')),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'О группе',
                'verbose_name_plural': 'О группе',
            },
        ),
        migrations.DeleteModel(
            name='AboutGroup',
        ),
    ]
