from django.urls import path
from core import views

urlpatterns = [
    path('about/', views.about, name = "about"),
    path('store/', views.store, name = "store"),
    path('', views.index, name = "index"),

]