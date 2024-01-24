from django.db import models
from django.utils import timezone


# class Movie(models.Model):
#     title = models.CharField(max_length=200)
#     year = models.IntegerField()

#     def __str__(self):
#         return f'title: {self.title} year: {self.year}'


class Member(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=10)


# class UserProfile(models.Model):
#     username = models.CharField(max_length=255, unique=True)
#     password = models.CharField(
#         max_length=255)  # In practice, use Django's built-in User model or hash passwords securely.

#     def __str__(self):
#         return self.username


# class Jaribu(models.Model):
#     name = models.CharField(max_length=255)
#     image = models.ImageField(upload_to='profiles/')
#
#     def __str__(self):
#         return self.name


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UserProfileManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, **extra_fields)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    # Add other fields as needed

    objects = UserProfileManager()

    USERNAME_FIELD = 'username'
    # Add any other required fields to REQUIRED_FIELDS if needed

    # Add related_name to avoid clashes with User model
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_profiles',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_profiles',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

    def __str__(self):
        return self.username


class Theater(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Screen(models.Model):
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    number = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.theater.name} - Screen {self.number}"


class Movie(models.Model):
    # Define the fields for the Movie model
    title = models.CharField(max_length=100)  # The title of the movie
    trailer = models.CharField(max_length=100, default='')
    synopsis = models.TextField(default='none')
    genre = models.CharField(max_length=50)  # The genre of the movie
    language = models.CharField(max_length=50)  # The language of the movie
    duration = models.CharField(max_length=50, default='')
    release_date = models.DateField()  # The release date of the movie
    price = models.DecimalField(max_digits=12, decimal_places=2)  # The price of the movie ticket
    image = models.ImageField(upload_to='movies/')  # The image of the movie poster
    # rating = models.FloatField()  # The average rating of the movie
    # reviews = models.TextField()  # The reviews of the movie
    CATEGORY_CHOICES = [
        ('top', 'Top'),
        ('latest', 'Latest'),
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='latest')
    # theaters = models.ManyToManyField(Theater)
    screens = models.ManyToManyField(Screen)

    def __str__(self):
        return self.title



