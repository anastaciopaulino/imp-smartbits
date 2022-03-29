from django.db import models
from apps.core.models import UUIDModel


class Event(UUIDModel):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    create_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name}'