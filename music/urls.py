from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:album_id>', views.detail),
    path('all', views.all),
]

