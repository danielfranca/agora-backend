from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class BorrowerUser(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="format expected: '+999999999'")
    register_regex = RegexValidator(regex=r'^\d{8}$', message="format expected: '99999999'")
    SECTORS = (
        ("RE", "Retail"),
        ("PS", "Professional Services"),
        ("FD", "Food & Drink"),
        ("EN", "Entertainment"),
    )

    user = models.ForeignKey(User)

    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=False, null=False)
    business_name = models.CharField(max_length=100, blank=False, null=False)
    business_address = models.CharField(max_length=255, blank=False, null=False)
    register_number = models.CharField(validators=[register_regex], max_length=8, blank=False, null=False)
    business_sector = models.CharField(max_length=2, choices=SECTORS)
