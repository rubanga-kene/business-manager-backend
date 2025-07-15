from django.urls import path
from . import views

urlpatterns = [
    # Categories
    path('categories/', views.CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', views.CategoryDetailAPIView.as_view(), name='category-detail'),
    path('categories/<int:pk>/update/', views.CategoryUpdateAPIView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', views.CategoryDestroyAPIView.as_view(), name='category-delete'),

    # Suppliers
    path('suppliers/', views.SupplierListCreateAPIView.as_view(), name='supplier-list-create'),
    path('suppliers/<int:pk>/', views.SupplierDetailAPIView.as_view(), name='supplier-detail'),
    path('suppliers/<int:pk>/update/', views.SupplierUpdateAPIView.as_view(), name='supplier-update'),
    path('suppliers/<int:pk>/delete/', views.SupplierDestroyAPIView.as_view(), name='supplier-delete'),

    # Products
    path('products/', views.ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', views.ProductDetailAPIView.as_view(), name='product-detail'),
    path('products/<int:pk>/update/', views.ProductUpdateAPIView.as_view(), name='product-update'),
    path('products/<int:pk>/delete/', views.ProductDestroyAPIView.as_view(), name='product-delete'),
    path('inventory-summary/', views.InventorySummaryAPIView.as_view(), name='inventory-summary'),
    path("category-distribution/", views.CategoryDistributionAPIView.as_view()),
]
