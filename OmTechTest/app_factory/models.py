from django.db import models

# Create your models here.
class CementFactoryInfo(models.Model):
    company_name = models.CharField(max_length=255)
    sector = models.CharField(max_length=100)
    email = models.EmailField()
    paid_up = models.IntegerField(help_text="Paid-up capital in rupees")

    def __str__(self):
        return f"Factory Information: {self.company_name}"


class NewsSectionInfo(models.Model):
    company = models.ForeignKey(CementFactoryInfo, on_delete=models.CASCADE, related_name='news')
    news_title = models.CharField(max_length=255)
    news_date = models.DateTimeField()
    news_image = models.ImageField(upload_to='news_images/')
    news_body = models.TextField()

    def __str__(self):
        return f"News Title: {self.news_title}"


class PriceHistoryInfo(models.Model):
    company = models.ForeignKey(CementFactoryInfo, on_delete=models.CASCADE, related_name='price_history')
    date = models.DateTimeField()
    open_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    close_price = models.FloatField()

    def __str__(self):
        return f"Price History on {self.date.strftime('%Y-%m-%d')} for {self.company.company_name}"
