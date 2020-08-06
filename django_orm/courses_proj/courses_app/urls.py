from django.urls import path
from . import views

urlpatterns={
    path('', views.index),
    path('courses/destroy/<int:id>',views.destroy),
    path('courses/new',views.new),
    path('courses',views.index),
}