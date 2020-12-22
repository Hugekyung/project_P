"""project_P URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accountapp.urls')), # accountapp안의 urls 파일을 참고해서 분기하게 한다.
    path('profiles/', include('profileapp.urls')), # project_P.urls: profiles + profileapp.urls: create ==> profiles/create/: 프로필 생성 화면으로 이동
    path('articles/', include('articleapp.urls')),
    path('comments/', include('commentapp.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # image를 가져오기 위한 라우팅 설정
