from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from blog import models

class BlogSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Blog
        fields = ['title', 'img', 'pub_date', 'like', 'comment']