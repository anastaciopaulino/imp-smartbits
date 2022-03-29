from django.db import models
from apps.core.models import UUIDModel

from random import randint


class Subject(UUIDModel):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f'{self.name}'
    
class Course(UUIDModel):
    name        = models.CharField(max_length=200)
    subjects    = models.ManyToManyField(Subject)
    description = models.TextField()
    create_at   = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name}'

CLASS_CHOICES = {
    ('13', '13'),
    ('12', '12'),
    ('11', '11'),
    ('10', '10')
}

class Subscription(UUIDModel):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    code = models.CharField(max_length=10, editable=False)
    _class = models.CharField(max_length=5, choices=CLASS_CHOICES)

    def __str__(self) -> str:
        return f'Subscription {self.name}'
    
    def save(self, *args, **kwargs):
        self.code = randint(10000, 90000)
        return super().save(*args, **kwargs)