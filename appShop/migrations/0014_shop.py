# Generated by Django 4.1.5 on 2023-06-19 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appShop', '0013_color_title2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('piece', models.IntegerField(verbose_name='Adet')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='Toplam Fiyat')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appShop.product', verbose_name='Ürün')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
        ),
    ]
