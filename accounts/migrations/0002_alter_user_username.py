# Generated by Django 4.2.2 on 2023-06-27 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.EmailField(help_text='Enter your Email', max_length=255, unique=True, verbose_name='Username'),
        ),
    ]