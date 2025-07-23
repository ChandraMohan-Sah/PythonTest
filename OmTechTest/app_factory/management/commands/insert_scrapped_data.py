import os, csv
from django.core.management.base import BaseCommand
from app_factory.models import CementFactoryInfo, PriceHistoryInfo
from datetime import datetime
from django.utils import timezone

class Command(BaseCommand):
    help = "Bulk insert Price History for Sarbottam Cement Limited"

    def handle(self, *args, **kwargs):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(BASE_DIR, 'data/price_data.csv')

        try:
            company = CementFactoryInfo.objects.get(company_name="Sarbottam Cement Limited")
        except CementFactoryInfo.DoesNotExist:
            print(" Company not found.")
            return

        with open(file_path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                date = timezone.make_aware(datetime.strptime(row['Date'], "%Y-%m-%d"))
                _, created = PriceHistoryInfo.objects.update_or_create(
                    company=company,
                    date=date,
                    defaults={
                        'open_price': float(row['Open']),
                        'high_price': float(row['High']),
                        'low_price': float(row['Low']),
                        'close_price': float(row['Ltp']),
                    }
                )
                status = "Inserted" if created else "Updated"
                print(f"{status}: {date.date()}")
