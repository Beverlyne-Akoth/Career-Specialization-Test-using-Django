"""careertest URL Configuration

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
from django.contrib import admin
from django.urls import path
from pages.views import home_view, page1_view, page2_view, page3_view, next1, next2, next3

urlpatterns = [
    path('', home_view, name='home'),
    path('page1/', page1_view),
    path('page2/', page2_view),
    path('page3/', page3_view),
    path('admin/', admin.site.urls),

    path('next_page1', next1),
    path('page1/next_page2', next2),
    path('page1/next_page3', next3),
]
