from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

class BbfList(APIView):

    def get(self, request):
        model= BbfData.objects.all()
        serializer=BbfSerializer(model, many=True)
        return Response(serializer.data)

class AddBbfCompany(APIView):

    def post(self, request):
        serializer=BbfSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BbfCompanyInfo(APIView):
    def get(self, request, company_abn):
        try:
            model= BbfData.objects.get(company_abn=company_abn)
        except BbfData.DoesNotExist:
            return Response('User not found', status=status.HTTP_404_NOT_FOUND)
        serializer=BbfSerializer(model)
        return Response(serializer.data)