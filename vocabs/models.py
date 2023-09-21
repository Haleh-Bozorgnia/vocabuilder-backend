from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Vocab(models.Model):
    vocab = models.CharField(max_length=200)
    translation = models.CharField(max_length=200)
    pronounciation = models.CharField(max_length=200)
    type = models.CharField(max_length=200)