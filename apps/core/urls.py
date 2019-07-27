from django.urls import path

from apps.core import views

urlpatterns = [
    path('test/', views.test, name='test'),
    path('', views.index, name='index'),

    #page path for a cuisine category id
    path('<int:cuisine_id>/', views.index),

    #page path for a specific recipe based on id
    path('recipe/<int:recipe_id>/', views.recipe, name='recipe'),

    #page path to save a recipe based on id
#    path('save-recipe/<int:recipe_id>/',views.save_recipe),
    
    path('save-recipe/', views.save_recipe),
]
