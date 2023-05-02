import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from .models import Book, Order,Cart
from django.views.generic import ListView,DetailView
from django .http import JsonResponse
from django.db.models import Q

# Create your tests here.

class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/About.html')
class BookListView(ListView):
    model = Book
    template_name = 'list.html'
class BookDetailView(DetailView):
    model = Book
    template_name = 'detail.html'
class BookCheckoutView(DetailView):
    model = Book
    template_name = 'checkout.html'
def PaymentComplete(request):
    body=json.loads(request.body)
    print('BODY:',body)
    product=Book.objects.get(id=body['productId'])
    Order.objects.create(product=product)
    return JsonResponse('Payment completed',safe=False)

class SearchResultsView(ListView):
    model= Book
    template_name = 'search.html'

    def get_queryset(self):
        query=self.request.GET.get('q')
        return Book.objects.filter(Q(title=query) | Q(author=query))
def add_to_cart(request,pk):
    Product = get_object_or_404(Book,pk=pk)
    cart_item,created = Cart.objects.get_or_create(
        user=request.user,
        product= Product,
        price=Product.price,
        image_url = Product.image_url,
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')


def remove_from_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, pk=cart_id, user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})


