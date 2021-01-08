from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from activity_log.models import UserMixin


User = get_user_model

class AccountManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, nik, password=None):
        if not email:
            raise ValueError('User harus memiliki email')
        if not first_name:
            raise ValueError('Tolong masukkan nama depan anda')
        if not last_name:
            raise ValueError('Tolong masukkan nama belakang anda')
        if not nik:
            raise ValueError('Tolong masukkan Nomor Induk Kependudukan anda')

        user = self.model(
                email = self.normalize_email(email),
                first_name = first_name,
                last_name = last_name,
                nik = nik
                )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, nik, password, *args, **kwargs):
        user = self.create_user(
                email = self.normalize_email(email),
                first_name = first_name,
                last_name = last_name,
                nik = nik,
                password=password,
                )
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user



class Acc(AbstractBaseUser):

    GENDER_CHOICE = (
        ('F', 'Perempuan'),
        ('M', 'Pria'),
        )

    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    first_name = models.CharField(verbose_name="nama depan", max_length=255)
    last_name = models.CharField(verbose_name="nama belakang", max_length=255)
    nik = models.CharField(verbose_name="nomor induk kependudukan", max_length=20)
    birth = models.DateField(default=None, verbose_name='ttl', null=True)
    gender = models.CharField(max_length=300, choices = GENDER_CHOICE, verbose_name='gender', blank=True)
    adress = models.TextField(verbose_name='alamat', blank=True)
    contact = models.CharField(max_length=20, verbose_name="nomor telepon", blank=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)

    # Make email as username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'nik']

    objects = AccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        # Simplest possible answer: Yes, always
        return True


# Only for LAST_ACTIVITY = True
class User(AbstractUser, UserMixin):
    pass
