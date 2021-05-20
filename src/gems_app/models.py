from django.db import models


class Deal(models.Model):
    customer = models.CharField(max_length=100, verbose_name='customer')
    item = models.CharField(max_length=100, verbose_name='item')
    total = models.FloatField(verbose_name='total')
    quantity = models.FloatField(verbose_name='quantity')
    date = models.DateTimeField(db_index=True, verbose_name='date')

    def __str__(self):
        return self.customer
