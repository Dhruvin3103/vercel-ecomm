# Generated by Django 4.2.2 on 2023-07-24 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catlog', '0006_remove_sizeproduct_size_sizeproduct_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sizeproduct',
            name='available_count',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AlterUniqueTogether(
            name='sizeproduct',
            unique_together={('size', 'product')},
        ),
    ]
