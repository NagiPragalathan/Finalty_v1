"""Finalty URL Configuration

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
from django.urls import path, include
from base.views import *


from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from Finalty import settings
from django.contrib.sitemaps.views import sitemap
from base.sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("underdev",underdev,name="underdev"),
    path("home",Home,name="home"),
    path("list_out",list_out,name="list_out"),
    path("delete_contact",delete_contact,name="delete_contact"),
    path("",Home,name="home"),
    path("underdev",underdev,name="underdev"),
    path("contact_form",contact_form,name="contact_form"),
    
    # Seo Config...
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', robots_txt),
]



urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)