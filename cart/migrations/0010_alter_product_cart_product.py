# Generated by Django 4.2.2 on 2023-07-24 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catlog', '0007_alter_sizeproduct_available_count_and_more'),
        ('cart', '0009_delete_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_cart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catlog.sizeproduct'),
        ),
    ]