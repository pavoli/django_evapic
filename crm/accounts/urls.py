from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('', views.home, name='home'),
    path('user/', views.user_page, name='user-page'),
    path('products/', views.products, name='products'),
    path('customer/<str:id>/', views.customer, name='customer'),

    path('create_order/<str:customer_id>/', views.create_order, name='create_order'),
    path('update_order/<str:id>/', views.update_order, name='update_order'),
    path('delete_order/<str:id>/', views.delete_order, name='delete_order'),
]
