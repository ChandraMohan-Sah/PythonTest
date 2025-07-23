# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('cement-factory-lc/', views.CementFactory_LC.as_view(), name='cement-factory-lc'),
    path('cement-factory-detail/<int:pk>/', views.CementFactory_Detail.as_view(), name="cement-factory-detail"),

    path('news-section-lc/', views.NewsSection_LC.as_view(), name="news-section-lc"),
    path('news-section-detail/<int:pk>/', views.NewsSection_Detail.as_view(), name="news-section-detail"),

    path('price-history-lc/',views.PriceHistory_LC.as_view(), name='price-history-lc'),
    path('price-history-detail/<int:pk>/', views.PriceHistory_Detail.as_view(), name='price-history-detail'),

    path('predict/', views.predict_next_numbers, name='predict_next_numbers'),

]
