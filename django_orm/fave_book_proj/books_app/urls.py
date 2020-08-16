from django.urls import path
from . import views

urlpatterns=[
    path('<int:id>/details',views.details),
    path('add_book',views.add_book),
    path('',views.books),
    path('<int:id>/edit',views.edit),
    path('<int:id>/like',views.like),
    path('<int:id>/delete',views.delete),
    path('logout',views.logout),
]