from django.urls import path

from api import views

urlpatterns=[
    path('<str:token>', views.home, name='Home'),
    path('', views.make, name='Make new'),
]