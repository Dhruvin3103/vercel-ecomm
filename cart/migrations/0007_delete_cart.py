# Generated by Django 4.2.2 on 2023-07-11 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_cart_payment_status_cart_price'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]