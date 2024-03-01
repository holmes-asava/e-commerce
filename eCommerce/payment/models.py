from django.db import models
from product.models import Product


# Create your models here.
class Transactions(models.Model):
    class Status(models.IntegerChoices):
        PENDING = 1
        COMPLETED = 2
        FAILED = 3
        CANCELLED = 4
        REFUNDED = 5

    status = models.IntegerField(choices=Status.choices,
                                 default=Status.PENDING)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.transaction_id


class TransactionItem(models.Model):
    transaction = models.ForeignKey(Transactions, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
