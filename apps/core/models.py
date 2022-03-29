import tempfile
import uuid

import requests
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

from .validators import latitude_validator, longitude_validator


class UUIDPrimaryKeyField(models.UUIDField):
    def __init__(self, *args, **kwargs):
        kwargs["primary_key"] = True
        kwargs["unique"] = True
        kwargs["editable"] = False
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        value = super().pre_save(model_instance, add)

        if value is None:
            value = uuid.uuid4()
            setattr(model_instance, self.attname, value)

        return value


class UUIDModel(models.Model):
    class Meta:
        abstract = True

    id = UUIDPrimaryKeyField()


class PointModel(UUIDModel):
    class Meta:
        abstract = True

    latitude = models.DecimalField(max_digits=10, decimal_places=8, validators=[latitude_validator])
    longitude = models.DecimalField(max_digits=11, decimal_places=8, validators=[longitude_validator])
    point = models.PointField()
    created_at = models.DateTimeField(auto_now_add=True)

    def _set_point(self):
        self.point = Point(x=float(self.longitude), y=float(self.latitude), srid=4326)

    def save(self, *args, **kwargs):
        self.clean_fields(exclude="point")
        self._set_point()
        super().save(*args, **kwargs)


class SimpleFetchedFile:
    def __init__(self, file_url=""):
        self.file = None
        if file_url:
            try:
                resp = requests.get(file_url)
                if resp.ok:
                    self.file = tempfile.NamedTemporaryFile()
                    self.file.write(resp.content)
            except Exception as e:
                print("Exception on apps.core.models.SimpleFetchedFile.__init__: " + str(e))