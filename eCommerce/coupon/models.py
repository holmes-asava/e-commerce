from django.db import models
from product.models import Product, ProductTag

# Create your models here.


class CouponCondition(models.Model):
    STATUS_CHOICES = (
        ('1', 'Active'),
        ('2', 'InActive'),
    )

    product_tag = models.ManyToManyField(ProductTag)
    product = models.ManyToManyField(Product)
    status = models.CharField(null=False, blank=False, max_length=8, choices=STATUS_CHOICES)


class Coupon(models.Model):

    COUPON_CHOICES = (
        ('1', 'Discount'),
        ('2', 'Free shipment'),
        ('3', 'New user'),
    )
    DISCOUNT_CHOICES = (
        ('1', 'Constant'),
        ('2', 'Percent'),
    )
    STATUS_CHOICES = (
        ('1', 'Active'),
        ('2', 'InActive'),
        ('3', 'Hidden'),
    )

    name = models.CharField(null=False, blank=False, max_length=255)
    type = models.CharField(null=False, blank=False, max_length=8, choices=COUPON_CHOICES)
    condition = models.ForeignKey(CouponCondition,on_delete=models.SET_NULL, null=True, blank=True)
    discount_amount = models.IntegerField(
        null=False,
        blank=False,
    )
    discount_type = models.CharField(null=False, blank=False, max_length=8, choices=COUPON_CHOICES)
    status = models.CharField(null=False, blank=False, max_length=8, choices=STATUS_CHOICES)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    token = models.CharField(null=False, blank=False, unique=True, max_length=32)
