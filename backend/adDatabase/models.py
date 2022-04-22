from django.db import models

# Basic ad model to store 1 image, title, info and a URL
class ad(models.Model):
    image = models.CharField(max_length=200)
    URL = models.CharField(max_length=50)
    adTitle = models.CharField(max_length=50)
    adInfo = models.CharField(max_length=200)

    def _str_(self):
        return self.adTitle