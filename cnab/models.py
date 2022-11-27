from django.db import models


class Cnab(models.Model):
    type_transaction = models.CharField(max_length=25)
    date = models.CharField(max_length=8)
    value = models.CharField(max_length=10)
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    hour = models.CharField(max_length=6)
    name_owner = models.CharField(max_length=14)
    name_company = models.CharField(max_length=19)
