from django.urls import path
from .views import *
urlpatterns=[
	path('login/',LoginApiView.as_view()),
	path('income/',GetData.as_view()),
]
