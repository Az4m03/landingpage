from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_page),
    path('thanks/', views.thanks_page, name='thanks_page')
]
