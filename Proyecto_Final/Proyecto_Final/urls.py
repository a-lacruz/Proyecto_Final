"""Proyecto_Final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from mvlcblog.views import (inicio, PostDetalle, PostList, 
                               PostCrear, PostBorrar, PostActualizar,
                               UserSignUp, UserLogin, UserLogout )
from django.contrib.admin.views.decorators import staff_member_required
urlpatterns = [
   
    path("admin/", admin.site.urls),
    path("mvlcblog/", inicio, name="mvlcblog-inicio"),
    path('mvlcblog/<int:pk>/detalle/', PostDetalle.as_view(), name="mvlcblog-detalle"),
    path("mvlcblog/listar/", PostList.as_view(), name="mvlcblog-listar"),
    path("mvlcblog/crear/", staff_member_required(PostCrear.as_view()), name="mvlcblog-crear"),
    path('mvlcblog/<int:pk>/borrar/', staff_member_required(PostBorrar.as_view()), name="mvlcblog-borrar"),
    path('mvlcblog/<int:pk>/actualizar/', staff_member_required(PostActualizar.as_view()), name="mvlcblog-actualizar"),
    path('mvlcblog/signup/', UserSignUp.as_view(), name ="mvlcblog-signup"),
    path('mvlcblog/login/', UserLogin.as_view(), name ="mvlcblog-login"),
    path('mvlcblog/logout/', UserLogout.as_view(), name ="mvlcblog-logout"),
    ]
