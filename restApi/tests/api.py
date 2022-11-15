from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


class UserAuth(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer=self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user= serializer.validated_data['user']
        token, created=Token.objects.get_or_create(user=user)
        return Response(token.key)

class CompanyList(APIView):

    def get(self, request):
        model= CompanyDetails.objects.all()
        serializer=companySerializer(model, many=True)
        return Response(serializer.data)


class CompanyListBbf(APIView):

    def get(self, request):
        model= CompanyDetails.objects.all().filter(data_from="BBF")
        serializer=companySerializer(model, many=True)
        return Response(serializer.data)

class CompanyListKinaway(APIView):

    def get(self, request):
        model= CompanyDetails.objects.all().filter(data_from="KINAWAY")
        serializer=companySerializer(model, many=True)
        return Response(serializer.data)

class AddCompany(APIView):

    def post(self, request):
        serializer=companySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CompanyInfo(APIView):
    def get(self, request, company_abn):
        try:
            model= CompanyDetails.objects.get(company_abn=company_abn)
        except CompanyDetails.DoesNotExist:
            return Response('User not found', status=status.HTTP_404_NOT_FOUND)
        serializer=companySerializer(model)
        return Response(serializer.data)

class CompanyContacted(APIView):

    def post(self, request, company_abn):
        try:
            model= CompanyDetails.objects.get(company_abn=company_abn)
        except CompanyDetails.DoesNotExist:
            return Response('User not found', status=status.HTTP_404_NOT_FOUND)
        serializer=companySerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CompanyIntersected(APIView):

    def post(self, request, company_abn):
        try:
            model= CompanyDetails.objects.get(company_abn=company_abn)
        except CompanyDetails.DoesNotExist:
            return Response('User not found', status=status.HTTP_404_NOT_FOUND)
        serializer=companySerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContactedCompanyListKinaway(APIView):

    def get(self, request):
        model= CompanyDetails.objects.all().filter(contacted=1, data_from="KINAWAY")
        serializer=companySerializer(model, many=True)
        return Response(serializer.data)

class NonContactedCompanyListKinaway(APIView):

    def get(self, request):
        model= CompanyDetails.objects.all().filter(contacted=0, data_from="KINAWAY")
        serializer=companySerializer(model, many=True)
        return Response(serializer.data)

class ContactedCompanyListBbf(APIView):

    def get(self, request):
        model= CompanyDetails.objects.all().filter(contacted=1, data_from="BBF")
        serializer=companySerializer(model, many=True)
        return Response(serializer.data)

class NonContactedCompanyListBbf(APIView):

    def get(self, request):
        model= CompanyDetails.objects.all().filter(contacted=0, data_from="BBF")
        serializer=companySerializer(model, many=True)
        return Response(serializer.data)

#Intersected Data API

class IntersectedCompanyListKinaway(APIView):

    def get(self, request):
        model= CompanyDetails.objects.all().filter(intersected=1, data_from="KINAWAY")
        serializer=companySerializer(model, many=True)
        return Response(serializer.data)

class NonIntersectedCompanyListKinaway(APIView):

    def get(self, request):
        model= CompanyDetails.objects.all().filter(intersected=0, data_from="KINAWAY")
        serializer=companySerializer(model, many=True)
        return Response(serializer.data)

class IntersectedCompanyListBbf(APIView):

    def get(self, request):
        model= CompanyDetails.objects.all().filter(intersected=1, data_from="BBF")
        serializer=companySerializer(model, many=True)
        return Response(serializer.data)

class NonIntersectedCompanyListBbf(APIView):

    def get(self, request):
        model= CompanyDetails.objects.all().filter(intersected=0, data_from="BBF")
        serializer=companySerializer(model, many=True)
        return Response(serializer.data)