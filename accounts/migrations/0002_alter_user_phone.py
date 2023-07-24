# Generated by Django 4.2.2 on 2023-07-24 07:59

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Enter Phone Number', max_length=128, null=True, region=None, unique=True),
        ),
    ]
