from coupon.models import Coupon
from django.db import models
from product.models import ProductDetail


# Create your models here.
class Transaction(models.Model):
    class Status(models.IntegerChoices):
        PENDING = 1
        COMPLETED = 2
        FAILED = 3
        CANCELLED = 4
        REFUNDED = 5
        SHIPMENT = 6

    status = models.IntegerField(choices=Status.choices,
                                 default=Status.PENDING)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True, blank=True)
    
    def cal_discount(self, coupon):

        if coupon.discount_type == '1':
            return sum([item.product.get_price() * item.quantity for item in self.transactionitem_set.all()]) - coupon.discount_amount
        elif coupon.discount_type == '2':
            return sum([item.product.get_price() * item.quantity for item in self.transactionitem_set.all()]) - (sum([item.product.get_price() * item.quantity for item in self.transactionitem_set.all()]) * coupon.discount_amount / 100)
        return sum([item.product.get_price() * item.quantity for item in self.transactionitem_set.all()]) - coupon.discount_amount
    
    def total_price(self):
        if self.coupon:
            return self.cal_discount(self.coupon)
        return sum([item.product.get_price() * item.quantity for item in self.transactionitem_set.all()])

class TransactionItem(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductDetail, on_delete=models.CASCADE)
    quantity = models.IntegerField()
