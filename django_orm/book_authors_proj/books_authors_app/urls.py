from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('view_book/<int:id>',views.view_book),
    path('author_details/<int:id>',views.author_details),
    path('add_book',views.add_book),
    path('add_author/<int:book_id>',views.add_author),
    path('view_authors',views.view_authors),
    path('create_author',views.create_author),
    path('delete_author',views.delete_author),
    path('add_book_to_author/<int:auth_id>',views.add_book_to_author),
    path('edit_book/<int:book_id>',views.edit_book),
]