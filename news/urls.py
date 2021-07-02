from django.urls import path

from .views import NewList


# app_name = 'news'

urlpatterns = [
    path('', NewList.as_view()),

]
