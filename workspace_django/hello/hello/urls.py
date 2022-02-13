"""hello URL Configuration

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
from django.urls import path , include
from . import views
# . 는 현재 같은 경로를 의미함

#아무것도 안들어오면 views.index로 연결해라 -> index의 함수로 간다
# 요청받아서 속해 있는 문자열을 response 한다 -> client한테 response

# path 쓰고 꼭 , 를 써야한다!!!!!
urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.index),
    path('hello01/', include('hello01.urls')),
    #hello01에 요청이 들어오면 hello01.urls에 연결해주세요
    # 한 군데서 모든 앱의 url을 관리하기 힘들어서 앱마다 url을 따로 만들어줬다.



]
