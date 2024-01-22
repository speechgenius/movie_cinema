"""
URL configuration for movies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from movies import views

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path("admin/", admin.site.urls),
                  # path("login", views.login),
                  path("seat", views.seatSelection, name='seat'),
                  path("login/", views.index, name='login'),
                  path('register', views.login_or_register, name='login_or_register'),
                  path('', views.netflixDisplay),
                  path('accounts/', include("django.contrib.auth.urls")),
                  path('netflix', views.read_json_from_file),
                  path('netflixDisplay', views.netflixDisplay, name='list'),
                  path('netflixToJson', views.netflixToJson),
                  path('card', views.cardPayment, name='cardPayment'),
                  path('movieDetails/<str:movie_id>/', views.movieDetails, name='details'),
                  path("listi", views.movieList, name='movieList'),
                  path('re/', views.register_user, name='register'),


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
