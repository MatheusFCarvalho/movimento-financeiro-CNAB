from django.db import models


class TypesOfTransactions(models.TextChoices):
    one = "Débito"
    two = "Boleto"
    three = "Financiamento"
    four = "Crédito"
    five = "Recebimento Empréstimo"
    six = "Vendas"
    seven = "Recebimento TED"
    eight = "Recebimento DOC"
    nine = "Aluguel"


class Cnab(models.Model):
    type_transaction = models.CharField(
        max_length=25, choices=TypesOfTransactions.choices)
    date = models.CharField(max_length=8)
    value = models.CharField(max_length=10)
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    hour = models.CharField(max_length=6)
    name_owner = models.CharField(max_length=14)
    name_company = models.CharField(max_length=19)
