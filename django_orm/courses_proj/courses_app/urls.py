from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    path('destroy/<int:id>',views.destroy),
    path('courses/new',views.new),
    # path('courses',views.index),
    path('prompt/<int:id>',views.prompt),
    path('comment/<int:id>',views.comment),
    path('<int:id>/add_comment',views.add_comment),
]