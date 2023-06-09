# Generated by Django 4.1.5 on 2023-05-31 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appShop', '0002_alter_brand_slug_alter_category_slug_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='piece',
        ),
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.IntegerField(default=5, verbose_name='Puan'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(default='', verbose_name='Yorum'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='title',
            field=models.CharField(default='', max_length=50, verbose_name='Yorum Başlık'),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating_total',
            field=models.FloatField(default=0, verbose_name='Puanlama'),
        ),
        migrations.AlterField(
            model_name='product',
            name='stok',
            field=models.IntegerField(default=0, verbose_name='Stok'),
        ),
        migrations.AlterField(
            model_name='product',
            name='text',
            field=models.TextField(default=models.CharField(max_length=50, verbose_name='Ürün Başlık'), verbose_name='Açıklama'),
        ),
    ]
