# Generated by Django 3.1.1 on 2020-09-08 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20200906_1954'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.RenameField(
            model_name='news',
            old_name='image',
            new_name='photo',
        ),
    ]
