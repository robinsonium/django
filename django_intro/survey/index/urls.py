from django.urls import path
from . import views
urlpatterns=[
    path('',views.index),
    path('result',views.result),
    path('render_result',views.render_result),
    path('start_over',views.start_over),
]