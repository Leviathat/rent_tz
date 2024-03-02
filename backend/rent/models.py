from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'products'


class Rent(models.Model):
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)

    @property
    def rent_duration(self):
        duration = self.end_date - self.start_date
        return duration.days

    @property
    def total_price(self):
        rent_products = RentProduct.objects.filter(rent=self)
        total_price = sum(
            rent_product.rent_price for rent_product in rent_products)
        return total_price * self.rent_duration

    class Meta:
        db_table = 'rents'


class RentProduct(models.Model):
    rent = models.ForeignKey(
        Rent, on_delete=models.CASCADE, related_name='rent_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rent_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'rent_products'
        unique_together = ('rent', 'product')
