from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.users.validators import UserPhoneNumberValidator
from apps.users.managers import CustomUserManager


class User(AbstractUser):
    class UserType(models.TextChoices):
        ADMIN = "admin", "Admin"
        STUDENT = "student", "Student"
        GUEST = "guest", "Guest"

    # Remove first_name and last_name from the parent model
    first_name = None
    last_name = None
    username = None

    # Add custom fields
    full_name = models.CharField("Full Name", max_length=255)
    role = models.CharField(max_length=16, choices=UserType.choices)
    avatar = models.ImageField(null=True, blank=True)

    # Phone number field with custom validation
    phone_number_validators = UserPhoneNumberValidator()
    phone_number = models.CharField(
        "Phone Number",
        validators=[phone_number_validators],
        max_length=255,
        unique=True
    )
    is_verified = models.BooleanField(default=False)

    # Set phone_number as the unique identifier for authentication
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []  # No additional required fields

    # Custom manager for handling user creation
    objects = CustomUserManager()

    def __str__(self):
        return self.full_name or self.phone_number
