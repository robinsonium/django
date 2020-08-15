from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('register',views.register),
    path('login',views.login),
    path('logout',views.logout),
    path('success',views.success),
    path('quotes',views.quotes),
    path('view_profile/<int:id>',views.view_profile),
    path('add_quote',views.add_quote),
    path('delete/<int:id>',views.delete),
    path('edit/<int:id>',views.edit),
    path('like/<int:id>',views.like),
]