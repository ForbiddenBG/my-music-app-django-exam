from django.core.exceptions import ValidationError


def alpha_numeric_validation(value):
    for ch in value:
        if not ch.isalnum() and '_' != ch:
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")
    return value
