from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, null=True, blank=True, unique=False)
    email = models.EmailField(max_length=254, unique=True)
    
    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        user = super().save(*args, **kwargs)
        user = CustomUser.objects.filter(email=self.email).first()
        UserProfile.objects.create(user=user)
        


class UserProfile(models.Model):
    user = models.OneToOneField("accounts.CustomUser",related_name="user_profile", on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username + " profile"
    
    class Meta:
        db_table = 'user_profiles'
        managed = True
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'