from django.db import models


class Failure(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    description = models.CharField(max_length=1000, blank=False)
    confirmed = models.BooleanField(default=True)
