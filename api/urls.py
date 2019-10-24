from django.urls import include, path, re_path
from django.contrib import admin
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'api', views.lambda_function)

urlpatterns = [
    path('', include(router.urls)),
]
