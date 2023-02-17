from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from api.views import BlogViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'blogs', BlogViewSet)


urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace="rest_framework")),
    path('', include(router.urls))
]
