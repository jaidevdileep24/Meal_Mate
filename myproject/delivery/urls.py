from django.urls import path,include
from . import views
from django.contrib import admin


app_name = 'delivery'

urlpatterns = [
    path('', views.home, name='home'),
    path('index',views.index,name = 'index'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('handle_signin/',views.handle_signin,name="handle_signin"),
    path('handle_signup/',views.handle_signup,name='handle_signup'),
    path('add_res/',views.add_res,name = 'add_res'),
    path('display_res/',views.display_res,name = 'display_res'),
    path('view_menu/<int:id>/',views.view_menu,name="view_menu"),
    path('add_menu/<int:id>/',views.add_menu,name="add_menu"),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('update_menu/<int:id>/',views.update_menu,name='update_menu'),
    path('cusdisplay/<str:username>/',views.cusdisplay, name = 'cusdisplay'),
    path('cusview_menu/<int:id>/<str:username>/',views.cusview_menu,name='cusview_menu'),
    path('show_cart/<str:username>/',views.show_cart, name = 'show_cart'),
    path('add_to_cart/<int:menuid>/<str:username>/',views.add_to_cart, name = 'add_to_cart'),
    path('checkout/<str:username>/',views.checkout,name='checkout'),
    path('orders/<str:username>',views.orders, name = 'orders'),
    
]
