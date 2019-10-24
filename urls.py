from django.urls import path, include, re_path
from django.contrib import admin
from rest_framework import routers
from api import views

urlpatterns = [
    path('', include(routers.DefaultRouter().urls)),
    path('admin/', admin.site.urls),
    # path('api/', include(('api.urls', 'api'), namespace='api')),
    path('lambda/', views.ListAPIView().as_view()),
#    re_path(r'response/(?P<pk>\d+)?', views.lambda_function.as_view())
]
