# Generated by Django 4.0.4 on 2022-05-26 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_remove_product_key_product_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(default='P_87B8', max_length=50, unique=True, verbose_name='Code'),
        ),
    ]