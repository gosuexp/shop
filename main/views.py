from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from cart.forms import CartAddProductForm

from . models import *
from . forms import *



class ShowMain(ListView):
    paginate_by = 3
    model = Product
    template_name = 'main/index.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cats = Category.objects.all()
        cart_product_form = CartAddProductForm()
        context['cats'] = cats
        context['cart_product_form'] = cart_product_form
        return context

    def get_queryset(self):
        return Product.objects.filter(is_published=True)


def category(request,cat_id):
    products = Product.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    cart_product_form = CartAddProductForm()
    return render(request, 'main/category.html', {
        'products' : products,
        'cats' : cats,
        'cart_product_form' : cart_product_form,
    })


class ShowPost(DetailView):
    model = Product
    template_name = 'main/post.html'
    context_object_name = 'products'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cats = Category.objects.all()
        cart_product_form = CartAddProductForm()
        context['cats'] = cats
        context['cart_product_form'] = cart_product_form
        return context




class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('main:home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cats = Category.objects.all()
        context['cats'] = cats
        context['title'] = 'Регистрация'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main:home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        cats = Category.objects.all()
        context['cats'] = cats
        return context

    def get_success_url(self):
        return reverse_lazy('main:home')


def logout_user(request):
    logout(request)
    return redirect('main:login')


class search(ListView):
    model = Product
    template_name = 'main/search.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cats = Category.objects.all()
        context['cats'] = cats
        return context

    def get_queryset(self):
        return Product.objects.filter(name__iregex=self.request.GET.get("search"))