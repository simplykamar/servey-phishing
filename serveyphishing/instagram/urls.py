
from django.urls import path
from .views import login,home,thanks

urlpatterns = [
    path('/login',login),
    path('',home),
    path('/thanks',thanks),

]
