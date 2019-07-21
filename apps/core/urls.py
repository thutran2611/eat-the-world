from django.urls import path

from apps.core import views

urlpatterns = [
    path('test', views.test_page, name='home'),
    path('about/', views.about, name='about'),
    path('',views.index, name='index'),
    path('recipe/',views.recipe, name='recipe'),
]
