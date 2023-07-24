# Generated by Django 4.2.2 on 2023-07-24 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catlog', '0002_sizechart_remove_product_available_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sizeproduct',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='catlog.product'),
        ),
        migrations.AlterField(
            model_name='sizeproduct',
            name='size',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='catlog.sizechart'),
        ),
        migrations.DeleteModel(
            name='Size',
        ),
    ]