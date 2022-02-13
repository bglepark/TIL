"""mymember URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from . import views
from django.contrib.auth import views as auth_views
# 같은 이름의 views가 되면 충돌 나니까 별칭 설정

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('register/' , views.register, name='register'), #자주 사용하는건 name 속성으로 등록
    path('login/' , auth_views.LoginView.as_view(template_name = 'login.html') , name = 'login'),
    path('logout/' , auth_views.LogoutView.as_view() , name = 'logout'),
    path('result/' , views.result , name='result'),

    
]
