from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(
            email=email,
            password=password,
            **extra_fields,
        )

    def create_superuser(self, email, password, **extra_fields):
        extra_fields['is_active'] = True
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True
        return self._create_user(
            email=email,
            password=password,
            **extra_fields,
        )


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        verbose_name=_("メールアドレス"),
        unique=True
    )

    username = models.CharField(
        verbose_name=_("ユーザー名"),
        max_length=150,
        null=True,
        blank=False
    )

    password = models.CharField(
        verbose_name=_("パスワード"),
        max_length=128,
    )

    profile = models.CharField(
        verbose_name=_("プロフィール"),
        max_length=150,
        null=True,
        blank=False
    )


    occupation = models.CharField(
        verbose_name=_("所属"),
        max_length=150,
        null=True,
        blank=False
    )

    position = models.CharField(
        verbose_name=_('役職'),
        max_length=150,
        null=True,
        blank=False
    )

    is_superuser = models.BooleanField(
        verbose_name=_("is_superuser"),
        default=False
    )

    is_staff = models.BooleanField(
        verbose_name=_('is_staff'),
        default=False,
    )
    
    is_active = models.BooleanField(
        verbose_name=_('is_active'),
        default=True,
    )


    objects = UserManager()

    USERNAME_FIELD = 'email' # ログイン時、ユーザー名の代わりにaccount_idを使用

    def __str__(self):
        return self.username