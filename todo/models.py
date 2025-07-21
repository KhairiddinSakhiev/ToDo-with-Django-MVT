from django.db import models
from datetime import timezone, datetime
from accounts.models import CustomUser as User



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