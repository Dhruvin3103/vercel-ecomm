# Generated by Django 4.2.2 on 2023-06-23 08:56

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(help_text='Enter your username', max_length=20, unique=True)),
                ('first_name', models.CharField(help_text='Enter your First name', max_length=20)),
                ('last_name', models.CharField(help_text='Enter your Last name', max_length=20)),
                ('date_of_birth', models.DateField(help_text='Enter your Date of Birth')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(help_text='Enter Phone Number', max_length=128, region=None, unique=True)),
                ('email', models.EmailField(help_text='Enter your Email', max_length=255, unique=True, verbose_name='email address')),
                ('email_token', models.CharField(blank=True, max_length=250, null=True)),
                ('phone_otp', models.IntegerField(blank=True, null=True)),
                ('password_reset_token', models.CharField(blank=True, max_length=250, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_email_verified', models.BooleanField(default=False)),
                ('is_phone_verified', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]