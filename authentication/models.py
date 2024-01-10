from django.db import models
from django.contrib.auth.models import AbstractUser
from django_otp.plugins.otp_totp.models import TOTPDevice
import random

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    otp = models.CharField(max_length=6, null=True, blank=True)

    def generate_otp(self):
        otp = str(random.randint(100000, 999999))
        self.otp = otp
        self.save()

        # Create TOTPDevice for the user
        totp_device = TOTPDevice.objects.create(user=self, confirmed=True)
        totp_device.save()

        # Send OTP via SMS here (use your SMS sending logic)
        return otp


    def __str__(self):
        return self.username
