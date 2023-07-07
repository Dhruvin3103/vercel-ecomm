# Generated by Django 4.2.2 on 2023-07-07 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='status',
            new_name='order_status',
        ),
        migrations.AddField(
            model_name='orders',
            name='payment_status',
            field=models.CharField(choices=[('1', 'paid'), ('2', 'Not paid')], default='2', max_length=200),
        ),
    ]
