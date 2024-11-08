from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from PIL import Image

from .managers import CustomUserManager
import datetime

#the custom user model
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Rider(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    image = models.ImageField(default="avatar.png", upload_to="rider_pics")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Lease(models.Model):
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
    start_date = models.DateField(blank=True,null=True)
    end_date = models.DateField(blank=True,null=True)
    amount = models.IntegerField(null=True,blank=True)
    is_active = models.BooleanField(default=True)
    paid = models.BooleanField(default=False)
    #national id as pdf or image
    national_id = models.FileField(upload_to="national_ids", blank=True, null=True)
    #driving license as pdf or image
    driving_license = models.FileField(upload_to="driving_licenses",blank=True,null=True)
    #introduction letter
    introduction_letter = models.FileField(upload_to="introduction_letters",blank=True,null=True)
    #passport photo
    passport_photo = models.ImageField(upload_to="passport_photos",blank=True,null=True)
    #next of kin national id
    next_of_kin = models.FileField(upload_to="next_of_kin_ids",blank=True,null=True)

    def __str__(self):
        return f"{self.rider.last_name} Lease"
    
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f"{self.name} Testimonial"