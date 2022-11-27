from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework.parsers import FileUploadParser
from .models import Cnab
from .serializers import CnabSerializer
from .arrays import type_transactions_data, negative_transactions
# Create your views here.
import ipdb


class UploadView(APIView):
    parser_classes = [FileUploadParser]
    queryset = Cnab
    serializer_class = CnabSerializer

    def post(self, request, filename):
        data = []
        files = request.FILES["file"].read().decode().split("\n")
        for file in files:
            type_number = int(file[:1])
            name_transaction_type = type_transactions_data[type_number]

            serializer = CnabSerializer(
                data={
                    "type_transaction": name_transaction_type,
                    "date": file[1:9],
                    "value": float(file[9:19])/100,
                    "cpf": file[19:30],
                    "card": file[30:42],
                    "hour": file[42:48],
                    "name_owner": file[48:62],
                    "name_company": file[62:81],
                }
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            data.append(serializer.data)

        return Response(data=data, status=201)


class ListView(APIView):
    queryset = Cnab
    serializer_class = CnabSerializer

    def get(self, request, name_company):
        import ipdb
        ipdb.set_trace()
        company_transactions = Cnab.objects.filter(
            name_company__icontains=name_company)

        list_all_transactions = []
        sum_all_values = 0

        for transaction in company_transactions:
            transaction_dict = dict(
                loja=transaction.name_company, tipo=transaction.type_transaction, valor=(
                    int(float(transaction.value)))
            )
            list_all_transactions.append(transaction_dict)

            if transaction.type_transaction in negative_transactions:
                sum_all_values -= int(float(transaction.value))
            else:
                sum_all_values += int(float(transaction.value))

        return Response({"Transações da Loja": list_all_transactions, "Saldo final": sum_all_values})
