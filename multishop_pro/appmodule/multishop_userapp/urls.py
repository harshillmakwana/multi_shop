from appmodule.multishop_userapp import views
from django.urls import path, include

urlpatterns = [
    path('myname/',views.myname, name='myname'),
    
    #pages
    path('',views.index_view, name='index_view'),
    path('shop_view/',views.shop_view, name='shop_view'),
    path('checkout_view/',views.checkout_view, name='checkout_view'),
    path('contact_view/',views.contact_view, name='contact_view'),
    path('pro_deatils_view/<int:id>/',views.pro_deatils_view, name='pro_deatils_view'),
        
    path('registration_view/',views.registration_view, name='registration_view'),
    path('login_view/',views.login_view, name='login_view'),
    path('logout_view/',views.logout_view, name='logout_view'),
    
    path('list_wishlist/',views.list_wishlist,name='list_wishlist'),
    path('add_to_wishlist/<int:product_id>/',views.add_to_wishlist,name='add_to_wishlist'),
    path('remove_wishlist/<int:product_id>/', views.remove_wishlist, name='remove_wishlist'),
    
    path('cart_view/',views.cart_view, name='cart_view'),
    path('cart_add/<int:id>/',views.cart_add, name='cart_add'),
    path('item_clear/<int:id>/',views.item_clear, name='item_clear'),
    path('item_increament/<int:id>/',views.item_increament, name='item_increament'),
    path('item_decreament/<int:id>/',views.item_decreament, name='item_decreament'),
    path('item_clear_all/',views.item_clear_all,name='item_clear_all'),
    
    path('address_view/',views.address_view,name='address_view'),
    path('payment_view/',views.payment_view,name='payment_view'),   
    path('payment_view/<int:id>/',views.payment_view,name='payment_view_with_id'),
    path('payment_success/',views.payment_success_view,name='payment_success'),
    path('payment_success/<str:order_id>/',views.payment_success_view,name='payment_success_with_id'),
    path('order_history/',views.order_history_view,name='order_history_view'),
    
    


    
    
]
