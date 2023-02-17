from blog.models import Blog
from rest_framework import routers, viewsets
from . import serializers

class BlogViewSet (viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = serializers.BlogSerializer
