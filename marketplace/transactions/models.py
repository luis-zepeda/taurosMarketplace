from django.db import models
from django.conf import settings

from marketplace.utils.models import MarketplaceModel


class Transaction(MarketplaceModel):
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    product = models.ForeignKey('products.Product', on_delete=models.PROTECT)
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL, related_name='buyer')
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.PROTECT, related_name='seller')
