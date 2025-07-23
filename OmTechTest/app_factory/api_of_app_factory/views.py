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

import numpy as np
from sklearn.linear_model import LinearRegression
from django.http import JsonResponse

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


def predict_next_numbers(request):
    data = PriceHistoryInfo.objects.values_list('close_price')

    X = np.arange(len(data)).reshape(-1, 1)
    y = np.array(data)

    # Training the model
    model = LinearRegression()
    model.fit(X, y)

    # Predicting next 5 steps: indexes 20,21,22,23,24
    X_future = np.arange(len(data), len(data) + 5).reshape(-1, 1)
    predictions = model.predict(X_future)

    # Convert predictions to a list and round values if needed
    predicted_list = predictions.tolist()

    return JsonResponse({'next_5_predictions': predicted_list})
