from appmodule.multishop_adminapp import views
from django.urls import path, include

urlpatterns = [
    path('myname/', views.myname, name='myname'),
    
    #pages
    path('index_view1/', views.index_view1, name='index_view1'),
    path('charts_view1/', views.charts_view1, name='charts_view1'),
    path('basic_elemrnta_view/', views.font_awesome_view, name='basic_elemrnta_view'),
    path('basic_table_view/', views.basic_table_view, name='basic_table_view'),
    path('blank_page_view/', views.blank_page_view, name='blank_page_view'),
    path('button_view/', views.button_view, name='button_view'),
    path('dropdowns_view/', views.dropdowns_view, name='dropdowns_view'),
    path('error_404_view/', views.error_404_view, name='error_404_view'),
    path('error_500_view/', views.error_500_view, name='error_500_view'),
    path('font_awesome_view/', views.font_awesome_view, name='font_awesome_view'),
    path('login_view1/', views.login_view1, name='login_view1'),
    path('register_view1/', views.register_view1, name='register_view1'),
    path('typography_view/', views.typography_view, name='typography_view'),
    
     
    #CRUD opration
    path('create_category/', views.create_category, name='create_category'),
    path('list_category/', views.list_category, name='list_category'),
    path('delete_category/<int:id>', views.delete_category, name='delete_category'),
    path('update_category/<int:id>', views.update_category, name='update_category'),
    
    path('create_category_sub/', views.create_category_sub, name='create_category_sub'),
    path('list_category_sub/', views.list_category_sub, name='list_category_sub'),
    path('delete_category_sub/<int:id>', views.delete_category_sub, name='delete_category_sub'),
    path('update_category_sub/<int:id>', views.update_category_sub, name='update_category_sub'),

    path('create_category_sub_sub/', views.create_category_sub_sub, name='create_category_sub_sub'),
    path('list_category_sub_sub/', views.list_category_sub_sub, name='list_category_sub_sub'),  
    path('delete_category_sub_sub/<int:id>', views.delete_category_sub_sub, name='delete_category_sub_sub'),
    path('update_category_sub_sub/<int:id>', views.update_category_sub_sub, name='update_category_sub_sub'),  
    
    path('create_product/', views.create_product, name='create_product'),
    path('list_product/', views.list_product, name='list_product'),
    path('delete_product/<int:id>', views.delete_product, name='delete_product'),
    path('update_product/<int:id>', views.update_product, name='update_product'),
    
    
    
      
]
