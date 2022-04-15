from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class ad(models.Model):
    image = models.CharField(max_length=200)
    URL = models.CharField(max_length=50)
    adTitle = models.CharField(max_length=50)
    adInfo=models.CharField(max_length=200)

    def _str_(self):
        return self.title