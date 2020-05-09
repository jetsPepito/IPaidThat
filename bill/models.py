from django.db import models

# Create your models here.
from django.db import models


class RetObject(models.Model):
    email = models.CharField(max_length=200)
    invoice_number = models.CharField(max_length=100)
    date = models.DateTimeField()
    client_name = models.CharField(max_length=200)
    total_ttc = models.CharField(max_length=50)
    total_vat = models.TextField(max_length=50)