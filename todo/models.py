from django.db import models
from django.contrib.auth.models import User
from datetime import timezone, datetime


class UserProfile(models.Model):
    user = models.OneToOneField(User,related_name="user_profile", on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13)
    image = models.ImageField()
    bio = models.TextField()

    def __str__(self):
        return self.user.username + " profile"
    
    class Meta:
        db_table = 'user_profiles'
        managed = True
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'


class Task(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, related_name="user_tasks", on_delete=models.CASCADE)
    due_date = models.DateTimeField(default=datetime.now())
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'tasks'
        managed = True
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'