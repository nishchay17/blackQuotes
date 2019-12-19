from django.urls import path
from . import views

urlpatterns = [
    path('', views.show, name='show'),
    path('All', views.all),
    path('Random', views.rand),
]