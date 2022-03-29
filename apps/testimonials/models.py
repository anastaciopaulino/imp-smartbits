from django.db import models
from apps.core.models import UUIDModel
from apps.core.upload import testemonial_directory_path

class Testimonial(UUIDModel):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to=testemonial_directory_path)
    create_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'Testimonial {self.name}'