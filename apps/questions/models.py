from django.db import models

from apps.core.models import UUIDModel

# Create your models here.
class Question(UUIDModel):
    question = models.TextField()
    response = models.TextField()

    create_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return '{}' .format(self.question[:50])
