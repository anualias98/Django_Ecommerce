from django import urls
from django.urls import path
from .import views
from .views import BookListView,BookDetailView,BookCheckoutView,PaymentComplete


urlpatterns=[
    path('book_list',BookListView.as_view(),name = 'list'),
    path('details/<int:pk>/',BookDetailView.as_view(),name='detail-view'),
    path('checkout/<int:pk>/',BookCheckoutView.as_view(),name='checkout-view'),
    path('complete',views.PaymentComplete,name='complete')

]