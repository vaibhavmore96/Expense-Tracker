from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.Index, name="Welcome to Expense Tracker",),
    path('about/', views.Index, name="about_us",),
    path('contact/', views.contact, name="contact_us", ),
    path('register/', views.Register, name="register", ),
    path('login/', views.login, name="login", ),
    path('logout/',views.logout, name="logout",),
    path('addexpense/',views.addexpense, name="addexpense",)
]

