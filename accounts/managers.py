from django.contrib.auth.models import BaseUserManager



class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email or not password:
            raise ValueError("Email and password must be set")
        email = self.normalize_email(email=email)
        user = self.model(email=email, **extra_fields)    # user = User(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email=email, password=password, **extra_fields)

        