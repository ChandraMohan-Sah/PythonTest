# views.py
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.exceptions import ValidationError

from app_factory.models import (
    CementFactoryInfo,
    NewsSectionInfo,
    PriceHistoryInfo
)

from .serializers import (
    CementFactorySerializer, 
    NewsSectionSerializer,
    PriceHistorySerializer
)


class CementFactory_LC(generics.ListCreateAPIView):
    queryset = CementFactoryInfo.objects.all()
    serializer_class = CementFactorySerializer


class CementFactory_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CementFactoryInfo.objects.all()
    serializer_class = CementFactorySerializer


class NewsSection_LC(generics.ListCreateAPIView):
    queryset = NewsSectionInfo.objects.all()
    serializer_class = NewsSectionSerializer
    

class NewsSection_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewsSectionInfo.objects.all()
    serializer_class = NewsSectionSerializer

class PriceHistory_LC(generics.ListCreateAPIView):
    queryset = PriceHistoryInfo.objects.all()
    serializer_class = PriceHistorySerializer 

class PriceHistory_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PriceHistoryInfo.objects.all()
    serializer_class = PriceHistorySerializer 
