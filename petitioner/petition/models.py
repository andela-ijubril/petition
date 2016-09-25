from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Petition(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()


class Signature(models.Model):
    petition = models.ForeignKey(Petition)
    time_signed = models.DateTimeField(default=timezone.now)
