# serializers.py
from rest_framework import serializers
from app_factory.models import (
    CementFactoryInfo,
    NewsSectionInfo,
    PriceHistoryInfo
)

class CementFactorySerializer(serializers.ModelSerializer):
    news = serializers.StringRelatedField(read_only=True)
    price_history = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = CementFactoryInfo
        fields = '__all__'
    

class NewsSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsSectionInfo
        fields = '__all__'
    

class PriceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceHistoryInfo
        fields = '__all__'


