# Generated by Django 4.0.4 on 2022-05-26 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_alter_product_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(default='P_A95G', max_length=50, unique=True, verbose_name='Code'),
        ),
    ]