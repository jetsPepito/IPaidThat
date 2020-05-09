from . import views
from django.urls import path
from django.conf.urls import url
from django.urls import path, include # new

app_name = 'bill'
urlpatterns = [
    path('login/', views.login, name='login'),
]