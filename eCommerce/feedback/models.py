from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class Feedback(models.Model):
    class FeedbackType(models.IntegerChoices):
        Transportation = 1
        Product = 2
        Service = 3
        Website = 4
        Other = 5

    score = models.IntegerField(null=False, blank=False,validators=[MinValueValidator(1), MaxValueValidator(5)])
    type = models.IntegerField(choices=FeedbackType.choices, default=FeedbackType.Transportation)
    customer = models.ForeignKey('customer.Customer', on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey('product.ProductDetail', on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey('payment.Transaction', on_delete=models.SET_NULL, null=True, blank=True)
    subject = models.CharField(max_length=255, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name
