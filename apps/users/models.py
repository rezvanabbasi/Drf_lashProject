import uuid
from django.contrib.auth.models import AbstractBaseUser, User
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserType(models.Model):
    title = models.CharField(max_length=10, default='زیباجو')
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        null=True
    )
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    username = models.CharField(max_length=300, unique=True, default='username')
    password = models.CharField(max_length=8, unique=True, default='password')
    full_name = models.CharField(max_length=300, null=True)
    image = models.ImageField(null=True)
    address = models.CharField(max_length=300, null=True)
    birth_date = models.DateField(null=True)
    user_type = models.ForeignKey(
        UserType,
        on_delete=models.CASCADE,
        related_name='user',
        null=True
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    uuid = models.CharField(_("uid"), max_length=300, default=uuid.uuid4())

    def __str__(self):
        return self.email

    def change_password(self, new_password):
        self.password = new_password
        self.user.password = new_password
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


class OtpCode(models.Model):
    mobile = models.CharField(max_length=11)
    code = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mobile
