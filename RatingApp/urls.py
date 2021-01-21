from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('About/', views.AboutPage, name='about'),
    path('products/', ProductPage.as_view(), name='products'),
    path('products/<p_slug>-details/', views.ProductDetailsPage, name='product-details'),

    path('auth/Register/', views.regView, name='register'),
    path('auth/login/', views.loginView, name='login'),
    path('auth/logout/', views.logoutView, name='logout')
]