# Generated by Django 4.2.10 on 2024-03-01 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0002_alter_coupon_discount_type'),
        ('product', '0002_alter_productstock_product'),
        ('payment', '0002_rename_transactions_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='coupon.coupon'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.IntegerField(choices=[(1, 'Pending'), (2, 'Completed'), (3, 'Failed'), (4, 'Cancelled'), (5, 'Refunded'), (6, 'Shipment')], default=1),
        ),
        migrations.AlterField(
            model_name='transactionitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productdetail'),
        ),
    ]
