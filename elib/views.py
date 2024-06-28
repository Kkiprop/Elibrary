from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from . models import Books, Cart, CartItem,Customer
from .forms import SearchForm
from django.urls import reverse
from django.conf import settings 
import stripe

def home(request):
    books = Books.objects.filter(availability=True)
    return render(request, 'home.html', {'books':books})

def success(request):
    return render(request, 'success.html')

def cancel(request):
    return render(request, 'cancel.html')

def book_detail(request, slug):
    book = get_object_or_404(Books, slug=slug)

    return render(request, 'book_details.html', {'book': book})

@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Books, id=book_id)
    cart, created = Cart.objects.get_or_create(user=request.user, defaults={'id': request.session.get('cart_id')})
    cart_item, created = CartItem.objects.get_or_create(book=book)
    cart.items.add(cart_item)
    request.session['cart_id'] = cart.id
    return redirect('elib:cart_detail')

    if not created:
        cart_item.increase_quantity()
    else:
        cart.items.add(cart_item)

@login_required
def increase_cart_item_quantity(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.increase_quantity()
    return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart = None
    total_price = 0
    if 'cart_id' in request.session:
        cart = Cart.objects.get(id=request.session['cart_id'])
        total_price = cart.get_total_price()
        cart_items = cart.items.all()

    stripe.api_key = settings.STRIPE_SECRET_KEY
    if request.method == "POST":
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    "price": item.book.stripe_price_id,
                    "quantity": 1,
                }
                for item in cart_items
            ],
            mode="payment",
            success_url=request.build_absolute_uri(reverse("elib:success")),
            cancel_url=request.build_absolute_uri(reverse("elib:cancel")),
        )
        return redirect(checkout_session.url, code=303)

    return render(request, 'cart_detail.html', {'cart': cart, 'total_price': total_price})

@login_required
def customer_dashboard(request):
    if 'cart_id' in request.session:
        cart = Cart.objects.get(id=request.session['cart_id'])
        cart_items = cart.items.all()
        total_price = cart.get_total_price()

    return render(request, 'dash.html', {'cart_items': cart_items, 'cart':cart, 'total_price':total_price})

@login_required
def remove_from_cart(request, item_id):
    cart = Cart.objects.filter(user=request.user).first()
    if cart:
        cart_item = get_object_or_404(CartItem, id=item_id, cart=cart)
        cart.items.remove(cart_item)
        cart_item.delete()
    
    return redirect('elib:cart_detail')

@login_required
def remove_from_dashboard(request, item_id):
    cart = Cart.objects.filter(user=request.user).first()
    if cart:
        cart_item = get_object_or_404(CartItem, id=item_id, cart=cart)
        cart.items.remove(cart_item)
        cart_item.delete()
    
    return redirect('elib:dashboard')


def search_view(request):
    form = SearchForm(request.GET)
    results = []

    if form.is_valid():
        query = form.cleaned_data['query']
        results = Books.objects.filter(title__icontains=query)

    context = {
        'form': form,
        'results': results,
    }
    return render(request, 'search_results.html', context)