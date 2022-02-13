"""tags URL Configuration

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
# 같은 디렉토리 (.) 에서 views.py를 가져올거다
# urls.py에서 아무것도 없이 요청이 되면 views.index 에 전달해라
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('var/' , include('var.urls')),
    path('statics/' , include('statics.urls')),

]
