from django.db import models


class ProductTag(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    product_tag = models.ForeignKey(ProductTag, on_delete=models.SET_NULL,null=True, blank=True)

    def __str__(self):
        return self.title


class ProductDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # TODO change to image list fields
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.product.description

    def get_image_url(self):
        return f"/media/{self.image}"

    def get_price(self):
        return self.price

    def current_stock(self):
        return ProductStock.objects.filter(product=self).aggregate(models.Sum('amount'))['amount__sum'] or 0
    
    
class ProductStock(models.Model):
    STATUS_CHOICES = (
        ('1', 'Deposite'),
        ('2', 'Withdrawal'),
    )

    product = models.ForeignKey(ProductDetail, on_delete=models.CASCADE)
    amount = models.IntegerField(null=False, blank=False)
    status = models.CharField(null=False, blank=False, max_length=8, choices=STATUS_CHOICES)
    created_by = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


