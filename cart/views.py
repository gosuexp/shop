from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404, render
from django.views.decorators.http import require_POST


from main.models import Product, Category
from .cart import Cart
from .forms import CartAddProductForm


# Create your views here.

@login_required
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'],update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


@login_required
def cart_detail(request):
    cart = Cart(request)
    cats = Category.objects.all()
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'], 'update': True
        })
    return render(request, 'cart/cart_detail.html', {
        'cart': cart,
        'cats' : cats
    })