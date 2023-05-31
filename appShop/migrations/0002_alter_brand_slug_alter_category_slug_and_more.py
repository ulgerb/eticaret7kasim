# Generated by Django 4.1.5 on 2023-05-31 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appShop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='slug',
            field=models.SlugField(blank=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='color',
            name='slug',
            field=models.SlugField(blank=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, verbose_name='slug'),
        ),
    ]