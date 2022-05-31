from django.urls import path
#from .views import index,new
from . import views


urlpatterns = [
    path('', views.index),
    path('new/', views.new)
]