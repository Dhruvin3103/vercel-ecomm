# Generated by Django 4.2.2 on 2023-07-03 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_user_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
    ]