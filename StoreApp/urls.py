from django.urls import include, path
from StoreApp import views


urlpatterns = [
    
    path('', views.index, name='index'),
]