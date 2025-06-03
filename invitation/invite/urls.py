from django.urls import path
from .import views

urlpatterns = [
    path('',views.show, name='home'),
    path('pre-register/', views.pre_register_user, name='pre_register'),
]