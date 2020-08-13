from django.urls import path
from . import views

urlpatterns=[
    path('show_wall',views.show_wall),
    path('add_comment',views.add_comment),
    path('delete_comment',views.delete_comment),
    path('add_message',views.add_message),
    path('',views.show_wall),
]


# totally works
# urlpatterns=[
#     path('',views.show_wall),
#     path('/add_comment',views.add_comment),
#     path('/delete_comment',views.delete_comment),
#     path('/add_message',views.add_message),
# ]