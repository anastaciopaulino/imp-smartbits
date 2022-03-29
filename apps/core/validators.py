from django.core.exceptions import ValidationError


def latitude_validator(latitude):
    if latitude < -90 or latitude > 90:
        raise ValidationError("Latitude value must be between -90 and 90.")


def longitude_validator(longitude):
    if longitude < -180 or longitude > 180:
        raise ValidationError("Longitude value must be between -180 and 180.")