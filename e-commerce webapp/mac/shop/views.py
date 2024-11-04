from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, SubCategory, Product
import logging
from django.contrib import messages

logger = logging.getLogger(__name__)

class HomeView(View):
    def get(self, request):
        return render(request, 'shop/home.html')

class CategoryListView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'shop/category_list.html', {'categories': categories})

class SubCategoryListView(View):
    def get(self, request, category_id):
        subcategories = SubCategory.objects.filter(category_id=category_id)
        return render(request, 'shop/subcategory_list.html', {
            'subcategories': subcategories,
            'category_id': category_id,
        })

class ProductListView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'shop/product_list.html', {'products': products})

class ProductDetailView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        return render(request, 'shop/product_detail.html', {'product': product})

class ProductBySubCategoryView(View):
    def get(self, request, category_id, subcategory_id):
        products = Product.objects.filter(sub_category_id=subcategory_id)
        return render(request, 'shop/products_by_subcategory.html', {'products': products})

class AddToCartView(View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        cart = request.session.get('cart', {})
        quantity = request.POST.get('quantity', 1)

        if product_id in cart:
            cart[product_id] += int(quantity)
        else:
            cart[product_id] = int(quantity)

        request.session['cart'] = cart

        logger.info(f'Cart updated: {cart}')
        
        messages.success(request, f'Added {quantity} of {product.name} to your cart.')
        
        logger.info(f'Added {quantity} of product {product_id} to cart. Current cart: {request.session.get("cart")}')
        
        return redirect('product_detail', pk=product_id)


class BuyNowView(View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        cart = request.session.get('cart', {})
        cart[product_id] = 1
        request.session['cart'] = cart
        logger.info(f'Buying product {product_id}.')
        return redirect('checkout')

class CartView(View):
    def get(self, request):
        cart = request.session.get('cart', {})
        logger.info(f'Current cart contents: {cart}')  
        
        products = Product.objects.filter(id__in=cart.keys())
        product_dict = {product.id: product for product in products}
        return render(request, 'shop/cart.html', {'products': product_dict, 'cart': cart})


class CheckoutView(View):
    def get(self, request):
        cart = request.session.get('cart', {})
        products = Product.objects.filter(id__in=cart.keys())
        return render(request, 'shop/checkout.html', {'products': products, 'cart': cart})




  

