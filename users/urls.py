from django.conf.urls import url
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    url('accounts/', include("django.contrib.auth.urls")),

    path('accounts/login/', views.user_login, name="login"),
]