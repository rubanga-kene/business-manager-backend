from rest_framework import serializers
from . models import Category, Supplier, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'



class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    supplier = SupplierSerializer(read_only=True)

    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )
    supplier_id = serializers.PrimaryKeyRelatedField(
        queryset=Supplier.objects.all(), source='supplier', write_only=True
    )

    class Meta:
        model = Product
        fields = [
            'id', 'product_name', 'product_description', 'quantity', 'unit_price',
            'm_date', 'e_date', 'category', 'supplier', 'category_id', 'supplier_id'
        ]