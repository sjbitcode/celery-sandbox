from django.db import models
from django.utils import timezone


class Link(models.Model):
    name = models.CharField(max_length=300)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(default=timezone.now)
    destination = models.URLField(max_length=300)

    def __str__(self):
        return '{} - {}'.format(self.name[:10], self.destination[:10])
