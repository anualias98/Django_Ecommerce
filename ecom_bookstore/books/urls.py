from django import urls
from django.urls import path
from .import views
from .views import BookListView, BookDetailView, BookCheckoutView, PaymentComplete, SearchResultsView, About

urlpatterns=[
    path('about/',About.as_view(),name='about'),
    path('book_list',BookListView.as_view(),name = 'list'),
    path('details/<int:pk>/',BookDetailView.as_view(),name='detail-view'),
    path('checkout/<int:pk>/z',BookCheckoutView.as_view(),name='checkout-view'),
    path('complete',views.PaymentComplete,name='complete'),
    path('search',SearchResultsView.as_view(),name='search'),
    path('cart/add/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart, name='cart'),

]