# Generated by Django 4.1.7 on 2023-04-08 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rewindgroup', '0017_remove_links_resourse_links_platform_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Цена билета'),
        ),
        migrations.AddField(
            model_name='concert',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Цена билета'),
        ),
    ]
