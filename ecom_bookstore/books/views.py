import json
from django.shortcuts import render
from .models import Book, Order
from django.views.generic import ListView,DetailView
from django .http import JsonResponse

# Create your tests here.


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
