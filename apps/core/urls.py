from django.urls import path

from apps.core import views

urlpatterns = [
    path('test/', views.test, name='test'),
    path('test/<int:id>/', views.test),
    path('about/', views.about, name='about'),
    path('', views.index, name='index'),
    path('<int:id>/', views.index),
    path('recipe/<int:id>/', views.recipe),
    path('recipe/', views.recipe, name='recipe'), 
]
