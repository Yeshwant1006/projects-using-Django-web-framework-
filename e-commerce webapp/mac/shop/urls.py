from django.urls import path
from .views import HomeView, CategoryListView, SubCategoryListView, ProductListView, ProductDetailView, ProductBySubCategoryView, AddToCartView, BuyNowView, CartView, CheckoutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:category_id>/subcategories/', SubCategoryListView.as_view(), name='subcategory_list'),
    path('categories/<int:category_id>/subcategories/<int:subcategory_id>/products/', ProductBySubCategoryView.as_view(), name='products_by_subcategory'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('add_to_cart/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('buy_now/<int:product_id>/', BuyNowView.as_view(), name='buy_now'),
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
]






