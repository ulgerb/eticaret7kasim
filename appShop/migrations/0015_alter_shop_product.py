# Generated by Django 4.1.5 on 2023-06-19 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appShop', '0014_shop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appShop.productdetail', verbose_name='Ürün'),
        ),
    ]
