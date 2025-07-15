from rest_framework import generics
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from . models import Category, Supplier, Product
from . serializers import CategorySerializer, SupplierSerializer, ProductSerializer

                # -----  CATEGORY VIEWS  -----------
# Create and List Viw
class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all().order_by('-id')
    serializer_class = CategorySerializer

# Detail view
class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Update category
class CategoryUpdateAPIView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_update(self, serializer):
        return super().perform_update(serializer)

# Delete category
class CategoryDestroyAPIView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
    


                          # -----  SUPPLIER VIEWS  -----------
                          
# List and Create Supplier
class SupplierListCreateAPIView(generics.ListCreateAPIView):
    queryset = Supplier.objects.all().order_by('-id')
    serializer_class = SupplierSerializer

# Retrieve Supplier
class SupplierDetailAPIView(generics.RetrieveAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

# Update Supplier
class SupplierUpdateAPIView(generics.UpdateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

# Delete Supplier
class SupplierDestroyAPIView(generics.DestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer



                            # -----  PRODUCTS VIEWS  -----------

# List and Create Product
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category']
    search_fields = ['product_name', 'category__category_name']

    # def get(self, request, *args, **kwargs):
    #     latest_product = Product.objects.order_by('-created_at').first()
    #     highest_quantity_product = Product.objects.order_by('-quantity').first()
    #     lowest_quantity_product = Product.objects.order_by('quantity').first()
    #     serializer = ProductSerializer([latest_product, highest_quantity_product, lowest_quantity_product], many=True)

    #     return Response({
    #         'latest_product':serializer.data[0],
    #         'lowest_quantity_product': serializer.data[1],
    #         'highest_quantity_product':serializer.data[2],
    #     })

# Retrieve Product
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Update Product
class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Delete Product
class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Summary
class InventorySummaryAPIView(APIView):
    def get(self, request):
        # Newest product (latest by created/ID)
        newest = Product.objects.order_by('-id').first()

        # Highest quantity product
        highest_quantity = Product.objects.order_by('-quantity').first()

        # Lowest quantity product (greater than zero to avoid out-of-stock)
        lowest_quantity = Product.objects.exclude(quantity=0).order_by('quantity').first()

        return Response({
            "newest": ProductSerializer(newest).data if newest else None,
            "highest_quantity": ProductSerializer(highest_quantity).data if highest_quantity else None,
            "lowest_quantity": ProductSerializer(lowest_quantity).data if lowest_quantity else None,
        })

# Category distribution
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category

class CategoryDistributionAPIView(APIView):
    def get(self, request):
        data = []
        for category in Category.objects.all():
            count = category.product_set.count()
            if count > 0:  # Only include if category has products
                data.append({
                    "name": category.category_name,
                    "value": count
                })
        return Response(data)
