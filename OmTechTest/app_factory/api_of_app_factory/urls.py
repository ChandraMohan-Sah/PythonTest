# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('cement-factory-lc/', views.CementFactory_LC.as_view(), name='cement-factory-lc'),
    path('cement-factory-detail/<int:pk>/', views.CementFactory_Detail.as_view(), name="cement-factory-detail"),

]
