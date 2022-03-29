from django.db import models

from apps.core.models import UUIDModel
from apps.core.upload import gallery_directory_path

class Gallary(UUIDModel):
    photo = models.ImageField(upload_to=gallery_directory_path)
    create_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.pk}'