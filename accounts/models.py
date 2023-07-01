from django.db import models
from .managers import UserManager
from django.contrib.auth.models import AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class User(AbstractBaseUser):
    first_name = models.CharField(max_length=20, help_text='Enter your First name')
    last_name = models.CharField(max_length=20, help_text='Enter your Last name')
    date_of_birth = models.DateField(help_text='Enter your Date of Birth', null=True, blank=True)
    phone = PhoneNumberField(null=True,blank=True,help_text='Enter Phone Number')
    username = models.EmailField(
        verbose_name='Users Email',
        max_length=255,
        unique=True,
        help_text='Enter your Email',
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        help_text='Enter your Email',
    )
    email_token =  models.CharField(max_length=250, null=True, blank=True)
    phone_otp = models.IntegerField(null=True, blank=True)
    password_reset_token = models.CharField(max_length=250, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    is_phone_verified = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username+', '+str(self.phone)

    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
    def is_verified(self):
        return (self.is_email_verified and self.is_phone_verified)
    
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=50)
    pincode = models.BigIntegerField()
    country = models.CharField(max_length=50, default="India")
    state = models.CharField(max_length=50, default="Maharastra")

    def __str__(self):
        return str(self.user) +' '+str(self.id)