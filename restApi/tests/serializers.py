from rest_framework import serializers
from tests.models import *

class companySerializer(serializers.ModelSerializer):
    company_name=serializers.CharField(required=False)
    company_abn=serializers.CharField(required=False)
    intersected=serializers.IntegerField(required=False)
    data_from=serializers.CharField(required=False)
    class Meta:
        model = CompanyDetails
        fields = '__all__'

class KinawaySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = KinawayData
        fields = '__all__'

class BbfSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BbfData
        fields = '__all__'