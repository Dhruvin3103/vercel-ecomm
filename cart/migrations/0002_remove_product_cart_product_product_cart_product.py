# Generated by Django 4.2.2 on 2023-07-11 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catlog', '0001_initial'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_cart',
            name='product',
        ),
        migrations.AddField(
            model_name='product_cart',
            name='product',
            field=models.ManyToManyField(to='catlog.product'),
        ),
    ]