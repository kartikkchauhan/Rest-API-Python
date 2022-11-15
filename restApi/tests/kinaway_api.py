from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

class KinawayList(APIView):

    def get(self, request):
        model= KinawayData.objects.all()
        serializer=KinawaySerializer(model, many=True)
        return Response(serializer.data)

class AddKinawayCompany(APIView):

    def post(self, request):
        serializer=KinawaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class KinawayCompanyInfo(APIView):
    def get(self, request, company_abn):
        try:
            model= KinawayData.objects.get(company_abn=company_abn)
        except KinawayData.DoesNotExist:
            return Response('User not found', status=status.HTTP_404_NOT_FOUND)
        serializer=KinawaySerializer(model)
        return Response(serializer.data)