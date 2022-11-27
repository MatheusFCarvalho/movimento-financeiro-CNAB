from rest_framework import serializers
from .models import Cnab

type_transactions_data = {1: "Débito", 2: "Boleto",
                          3: "Financiamento",
                          4: "Crédito",
                          5: "Recebimento Empréstimo",
                          6: "Vendas",
                          7: "Recebimento TED",
                          8: "Recebimento DOC",
                          9: "Aluguel"}


class CnabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cnab
        fields = "__all__"


class FilesSerializer(serializers.Serializer):
    file = serializers.FileField()

    class Meta:
        fields = ["file"]
