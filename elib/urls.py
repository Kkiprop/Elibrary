from django.urls import path
from elib import views
from . views import home,book_detail,add_to_cart, cart_detail,success,cancel,customer_dashboard,remove_from_cart,remove_from_dashboard

app_name = 'elib'
urlpatterns = [
    path('', views.home, name='home'),
    path('book_detail/<slug:slug>/', views.book_detail, name='book_detail'),
    path('add-to-cart/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('cart_detail/', cart_detail, name='cart_detail'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
    path('dashboard/', views.customer_dashboard, name='dashboard'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('remove_from_dashboard/<int:item_id>/', views.remove_from_dashboard, name='remove_from_dashboard'),
    path('search/', views.search_view, name='search'),
]