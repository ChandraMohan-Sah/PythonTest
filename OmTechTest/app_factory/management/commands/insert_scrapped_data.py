import csv
from django.core.management.base import BaseCommand
from app_factory.models import CementFactoryInfo, PriceHistoryInfo
from django.utils.timezone import make_aware
from datetime import datetime

class Command(BaseCommand):
    help = "Insert Sarbottam Cement price history"

    def handle(self, *args, **kwargs):
        company = CementFactoryInfo.objects.filter(company_name="Sarbottam Cement Limited").first()
        if not company:
            print("Company not found"); return

        with open("app_factory/management/commands/data/price_data.csv") as f:
            for row in csv.DictReader(f):
                date = make_aware(datetime.strptime(row['Date'], "%Y-%m-%d"))
                obj, created = PriceHistoryInfo.objects.update_or_create(
                    company=company, date=date,
                    defaults={k: float(row[k]) for k in ['Open', 'High', 'Low', 'Ltp']}
                )
                print(f"{'Inserted' if created else 'Updated'}: {date.date()}")
