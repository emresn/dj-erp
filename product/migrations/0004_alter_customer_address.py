# Generated by Django 4.0.4 on 2022-05-21 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_customer_address_customer_bankaccount_customer_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.TextField(max_length=300, null=True, verbose_name='Address'),
        ),
    ]