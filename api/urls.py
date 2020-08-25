from django.urls import path

from api import views

urlpatterns=[
    path('<str:token>',views.Home, name='Home'),
    path('',views.Make , name='Make new'),
]