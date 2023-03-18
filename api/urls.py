from django.urls import path
from . import views

urlpatterns=[
    path('test', views.test, name="test"),
    path('generate_api', views.generate_api, name="generate_api")
]