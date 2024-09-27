from django.core import validators
from django.utils.deconstruct import deconstructible


@deconstructible
class UserPhoneNumberValidator(validators.RegexValidator):
    regex = r'^\+998\d{9}$'
    message = "Please enter your phone number in +998xxxxxxx format"
    flags = 0