# Generated by Django 4.2.2 on 2023-07-25 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catlog', '0008_rename_sizeproduct_productbysize'),
        ('order', '0008_remove_orders_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catlog.productbysize'),
        ),
    ]
