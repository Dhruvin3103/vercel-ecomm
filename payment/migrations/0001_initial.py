# Generated by Django 4.2.2 on 2023-07-18 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0007_merge_0004_orders_size_0006_delete_cartorder'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.CharField(max_length=200, verbose_name='Payment ID')),
                ('order_id_1', models.CharField(max_length=200, verbose_name='Order ID')),
                ('signature', models.CharField(blank=True, max_length=500, null=True, verbose_name='Signature')),
                ('amount', models.IntegerField(verbose_name='Amount')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('order_id_2', models.ManyToManyField(to='order.orders')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
