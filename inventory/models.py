from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    category_description = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.category_name


class Supplier(models.Model):
    supplier_name = models.CharField(max_length=200)
    supplier_contact = models.CharField(max_length=15)
    supplier_address = models.CharField(max_length=200)

    def __str__(self):
        return self.supplier_name


class Product(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    supplier = models.ForeignKey(Supplier, null=True, on_delete=models.SET_NULL)
    product_name = models.CharField(max_length=200)
    product_description = models.CharField(max_length=200, null=True, blank=True)
    quantity = models.IntegerField(default=0)
    unit_price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    m_date = models.DateField(null=True, blank=True)
    e_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name
