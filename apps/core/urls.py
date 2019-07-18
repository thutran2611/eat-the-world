from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.test_page, name='home'),
    path('about/', views.about, name='about'),
]
