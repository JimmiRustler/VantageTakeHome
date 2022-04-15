from pydoc import describe
from sre_constants import MAX_UNTIL
from unittest.util import _MAX_LENGTH
from xml.dom.minidom import CharacterData
from django.db import models
from django.forms import CharField

# Create your models here.
class AdInfo(models.Model):
    image=models.CharField(max_length=1500)
    webPageAddress=models.CharField(max_length=100)
    description=models.CharField(max_length=150)
    adInfo=models.CharField(max_length=150)


# string representation of the class
    def __str__(self):
 
        #it will return the title
        return self.title