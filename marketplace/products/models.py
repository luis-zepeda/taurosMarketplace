from django.db import models
from django.conf import settings

from marketplace.utils.models import MarketplaceModel

class Product(MarketplaceModel):
    name = models.CharField(max_length=255, null=False)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=False)
    quantity = models.IntegerField(null=False)
    is_active = models.BooleanField(default=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=False)
