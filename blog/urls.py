from django.contrib import admin
from django.urls import path
from blog.views import signup, log_in, workspace, Login, accueil
from blog.views import Login 



app_name = 'blog'

urlpatterns = [
    path('signup/', signup, name='register'),
    path('login/', log_in, name='login'),
    path('', accueil, name="home"),
    path('workspace/', workspace, name="workspace")
]
