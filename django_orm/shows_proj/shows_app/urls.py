from django.urls import path
from . import views

urlpatterns=[
    path('',views.index), #will redirect to /shows
    path('shows', views.shows, name="all_shows"),
    path('shows/new',views.new, name="my_new"),
    path('details/<int:show_id>/edit',views.edit, name="my_edit"),
    path('shows/<int:show_id>/delete',views.destroy, name="my_destroy"),
    path('details/<int:show_id>',views.details, name="my_details"),
    # path('details/<int:show_id>update',views.update, name="my_update"),
]