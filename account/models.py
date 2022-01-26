from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, category, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            category=category,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, category, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            category=category,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    CUSTOMER = 'Customer'
    RESTAURANT_MANAGER = 'Restaurant Manager'
    XXX = '***'

    CATEGORY = [
        (CUSTOMER, 'Customer'),
        (RESTAURANT_MANAGER, 'Restaurant Manager'),
        (XXX, '***')
    ]
    email = models.CharField(verbose_name="Email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name="Date Joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="Last Login", auto_now=True)
    category = models.CharField(max_length=18, choices=CATEGORY, default=CUSTOMER, blank=False)
    profile_image = models.ImageField(upload_to='image_uploads', max_length=100, default='image_uploads/ques.jpeg')
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'category']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
