from django.urls import path
from . import views

urlpatterns = [
    path('', views.shows),
    path('new', views.new),
    path('create', views.create),
    path('<int:show_id>/edit', views.edit),
    path('<int:show_id>/update', views.update),
    path('<int:show_id>', views.show),
    path('<int:show_id>/delete', views.delete),
]