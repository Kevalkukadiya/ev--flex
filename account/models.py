from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractUser
from django.utils.timezone import now



#  Custom User Manager
class UserManager(BaseUserManager):
  def create_user(self, email, username ,password=None):
      """
      Creates and saves a User with the given email, name and password.
      """
      if not email:
          raise ValueError('User must have an email address')

      user = self.model(
          email=self.normalize_email(email),
          username=username,
      )

      user.set_password(password)
      user.save(using=self._db)
      return user

  def create_superuser(self, email, username,  password=None):
      """
      Creates and saves a superuser with the given email, name and password.
      """
      user = self.create_user(
          email,
          password=password,
          username=username,
      )
      user.is_admin = True
      user.save(using=self._db)
      return user

        #  Custom User Model


class User(AbstractUser):
    email = models.EmailField(
      verbose_name='Email',
      max_length=255,
      unique=True,
      )
    TYPE_CHOICE = (
            ("OWNER", "OWNER"),
            ("CUSTOMER", "CUSTOMER")
            )
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length = 50, unique= True, null=True)
    first_name = models.CharField(max_length = 50, null=True)
    last_name = models.CharField(max_length = 50, null=True)
    user_type = models.CharField(max_length=9, choices=TYPE_CHOICE, default='CUSTOMER')
    address = models.CharField(max_length=255, null=True)
    mobile_number = models.CharField(max_length=25)
    date_of_birth = models.DateField(default=now, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_by = models.IntegerField(default=1, unique=False)
    deleted = models.IntegerField(default=0, unique=False)
    created_at = models.DateTimeField(default=now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin