from django.urls import path

from apps.core import views

urlpatterns = [
    path('test/', views.test, name='test'),
    path('test/<int:id>/', views.test),
    path('about/', views.about, name='about'),
    path('', views.index, name='index'),

    #page path for a cuisine category id
    path('<int:id>/', views.index),

    #page path for a specific recipe based on id
    path('recipe/<int:id>/', views.recipe),
    path('recipe/', views.recipe, name='recipe'), 
]
