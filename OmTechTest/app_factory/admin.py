from django.contrib import admin
from .models import CementFactoryInfo, NewsSectionInfo, PriceHistoryInfo

# Register your models here.
admin.site.register(CementFactoryInfo)
admin.site.register(NewsSectionInfo)
admin.site.register(PriceHistoryInfo)