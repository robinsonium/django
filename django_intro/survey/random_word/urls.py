from django.urls import path
from . import views

urlpatterns=[
    path('',views.random_word),
    path('/current_status',views.current_status),
    path('/generate',views.generate),
    path('/reset',views.reset),
]