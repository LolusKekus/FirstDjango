"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from landing import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^landing/$', views.landing, name='landing'),
    url(r'^phone/$', views.Phone.as_view(), name='phone'),
    url(r'^notebook/$', views.Notebook.as_view(), name='notebook'),
    url(r'^categoryes/(?P<category_id>\d+)/$', views.ProductListView.as_view(),
        name='categoryes'),
    url(r'^detail/(?P<pk>\d+)/$', views.ProductDetail.as_view(), name='detail'),
]
