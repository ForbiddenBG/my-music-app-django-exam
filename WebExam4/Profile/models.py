from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from core.validators import alpha_numeric_validation


# Create your models here.
class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=(
            MinLengthValidator(2),
            alpha_numeric_validation,
                    ),
    )

    email = models.EmailField(
    )

    age = models.IntegerField(
        validators=(
            MinValueValidator(0),
        ),
        null=True,
        blank=True,
    )
