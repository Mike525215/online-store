from django.shortcuts import render, redirect
from .models import *
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.views import LoginView
from .forms import *
from django.http import HttpResponse
from django.contrib.auth import login, logout
from .forms import *
class MainPage(ListView):
    model = Category
    template_name = 'projectApp/index.html'
    context_object_name = 'categories'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'MAIN PAGE'
        return context

class AllProducts(ListView):
    model = Items
    template_name = 'projectApp/all_items.html'
    context_object_name = 'items'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'ALL PRODUCTS'
        context['categories'] = Category.objects.all()
        return context

class CategoryItems(ListView):
    model = Items
    template_name = 'projectApp/category_items.html'
    context_object_name = 'category_items'

    def get_queryset(self):
        return Items.objects.filter(cat__slug=self.kwargs['cat_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['cat_slug']).name
        context['categories'] = Category.objects.all()
        return context

class Item(DetailView):
    model = Items
    template_name = 'projectApp/item.html'
    slug_url_kwarg = 'item_slug'
    context_object_name = 'item'

    def get_queryset(self):
        return Items.objects.filter(slug=self.kwargs['item_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_queryset()[0].title
        context['categories'] = Category.objects.all()
        return context

def add_item_cart(request):
    data = request.GET['item_id']
    if int(data) in [x.item.id for x in Cart.objects.filter(item_id=data, user=request.user)]:
        item = Cart.objects.get(item__id=data, user=request.user)
        item.count_item += 1
        item.save()
        return redirect('cart')
    else:
        item = Items.objects.get(id=data)
        form = Cart.objects.create(item=item, user=request.user)
        form.save()
        return redirect('cart')

def del_cart_item(request):
    data = request.GET['item_id']
    form = Cart.objects.filter(item_id=data, user=request.user)
    form.delete()
    return redirect('cart')

def count_item_up(request):
    data = request.GET['item_id']
    item = Cart.objects.get(item__id=data, user=request.user)
    item.count_item += 1
    item.save()
    return redirect('cart')

def count_item_down(request):
    data = request.GET['item_id']
    item = Cart.objects.get(item__id=data, user=request.user)
    item.count_item -= 1
    item.save()
    if item.count_item == 0:
        item.delete()
        return redirect('cart')
    else:
        return redirect('cart')

class CartItems(ListView):
    model = Cart
    template_name = 'projectApp/cart.html'
    context_object_name = 'items'
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def total_bill(self):
        return sum([x.item.price * x.count_item for x in Cart.objects.filter(user=self.request.user)])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Cart'
        context['cart'] = len(Cart.objects.filter(user=self.request.user)) > 0
        context['total_bill'] = self.total_bill()
        return context

def add_favorite_item(request):
    data = request.GET['item_id']
    if int(data) in [x.item.id for x in Favourites.objects.filter(user=request.user)]:
        return redirect('favorites')
    else:
        item = Items.objects.get(id=data)
        form = Favourites.objects.create(item=item, user=request.user)
        form.save()
        return redirect('favorites')
def del_favorite_item(request):
    data = request.GET['item_id']
    item = Favourites.objects.filter(item__id=data, user=request.user)
    item.delete()
    return redirect('favorites')

class Favorites(ListView):
    model = Favourites
    template_name = 'projectApp/favorites.html'
    context_object_name = 'items'

    def get_queryset(self):
        return Favourites.objects.filter(user=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Favorites'
        context['favorites'] = len(Favourites.objects.filter(user=self.request.user)) > 0
        return context

class Registration(CreateView):
    form_class = RegistrationForm
    template_name = 'projectApp/registration.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'REGISTRATION'
        return context


class Authentication(LoginView):
    form_class = LoginUserForm
    template_name = 'projectApp/login.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'AUTHENTICATION'
        return context

    def get_success_url(self):
        return reverse_lazy('home')

def logout_method(request):
    logout(request)
    return redirect('home')