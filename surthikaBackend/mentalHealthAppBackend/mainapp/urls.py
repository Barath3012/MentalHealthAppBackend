from django.urls import path
from .views import *
urlpattern=[path('questionare/',QuestionareView.as_view())]