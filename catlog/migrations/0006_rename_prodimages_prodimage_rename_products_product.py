# Generated by Django 4.2.2 on 2023-06-25 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catlog', '0005_rename_subcateorgy_products_sub_cateorgy_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProdImages',
            new_name='ProdImage',
        ),
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]
