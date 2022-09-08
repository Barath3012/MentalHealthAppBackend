from .views import *
from django.urls import path

urlpatterns=[
    path('login/',LoginApiView.as_view())
]