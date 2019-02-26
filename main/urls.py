"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path

from facebook.views import play
from facebook.views import play2
from facebook.views import test
from facebook.views import profile
from facebook.views import event
from facebook.views import fail
from facebook.views import help
from facebook.views import warn
from facebook.views import newsfeed
from facebook.views import detail_feed
from facebook.views import new_feed
from facebook.views import pages

urlpatterns = [
    path('admin/', admin.site.urls),
    path('play/', play),
    path('play2/', play2),
    path('test/', test),
    path('sean/profile/', profile),
    path('event/', event),
    path('fail/', fail),
    path('help/', help),
    path('warn/', warn),
    path('', newsfeed),
    path('feed/<pk>/', detail_feed),
    path('new/', new_feed),
    path('pages/', pages)
]
