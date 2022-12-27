from django.urls import path
from .views import *

urlpatterns = [
    path('', MainPage.as_view(), name='home'),
    path('all_items/', AllProducts.as_view(), name='items'),
    path('items/<slug:cat_slug>/', CategoryItems.as_view(), name='category_items'),
    path('item/<slug:item_slug>/', Item.as_view(), name='item'),
    path('add_item_cart/', add_item_cart, name='add_item_cart'),
    path('del_cart_item/', del_cart_item, name='del_cart_item'),
    path('count_item_up/', count_item_up, name='count_item_up'),
    path('count_item_down/', count_item_down, name='count_item_down'),
    path('cart/', CartItems.as_view(), name='cart'),
    path('add_favorite_item/', add_favorite_item, name='add_favorite_item'),
    path('del_favorite_item/', del_favorite_item, name='del_favorite_item'),
    path('favorites/', Favorites.as_view(), name='favorites'),
    path('registration/', Registration.as_view(), name='reg'),
    path('login/', Authentication.as_view(), name='login'),
    path('logout/', logout_method, name='logout')
]