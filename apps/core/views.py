from django.shortcuts import render, redirect
from django import forms
from .models import Cuisine, SavedRecipe
from . import utils
from . import tests
from apps.accounts.models import User
from django.contrib.auth import authenticate

class CuisineForm(forms.Form):
#    class Meta:
#        model = Cuisine
#        fields = ['name']
#        widgets = {
#            #can't figure out how to query db objects to populate drop-down
#            'name': forms.Select()
#        }
    cuisine = forms.ModelChoiceField(queryset=Cuisine.objects.order_by('name'))

#Views based on the template Reuben and Kyle are working on
def index(request, cuisine_id=0):
    
       
    #list of cuisines
    list_of_cuisines = Cuisine.objects.order_by('name')
    selected_cuisine = None
    rando_py = None
    
    #if a cuisine is provided get 
    if cuisine_id > 0:
        selected_cuisine = Cuisine.objects.get(id=cuisine_id)
        
        print('the selected cuisine is ->',selected_cuisine)
        
        rando = utils.get_recipe_by_cuisine(selected_cuisine)
        
        print('get_recipe_by_cuisine',rando)
        #convert to python
        rando_py = rando.json()
        print('rando_py',rando_py)
        
    else:
        print('no selected cuisine provided')


    context = {
        'list_of_cuisines': list_of_cuisines,
        'selected_cuisine': selected_cuisine,
        'recipe': rando_py,
        
    }
    return render(request, 'pages/index.html',context)

def recipe(request, recipe_id=0):
    details_py = None
    
    if recipe_id > 0:
        #get recipe details
        details = utils.get_recipe_details(recipe_id)
        
        details_py = details.json()
    else:
        print('Call to get recipe details without a recipe id')
        print(request)
    
    context = {
        "recipe": details_py,
    }

    return render(request, 'pages/recipe.html',context)


# Views for test page for trying out stuff, including test api calls returning python text
def test(request):
    print('test request')
    
    cuisine = None
    selected_cuisine = None
    rando = None
    details = None
    
    
    #Get list of cuisines from database since no way to dynamically pull from spoonful API
    list_of_cuisines = CuisineForm()
    
    # TODO figure out how request will be coming in for a recipe
    #Get 1 recipe if request includes a cuisine
    if 'cuisine' in request.GET:
        selected_cuisine_id = request.GET['cuisine']
        selected_cuisine = Cuisine.objects.get(id=selected_cuisine_id)
        
        print('the selected cuisine is ->',selected_cuisine)
    else:
        print('no selected cuisine provided')

    if selected_cuisine:
        rando = utils.get_recipe_by_cuisine(selected_cuisine)
        
        #convert to python
        rando_py = rando.json()
        
        #pull recipe ID out of the random recipe result
        rando_id = rando_py["results"][0]["id"]
        print('rando recipe ID is ->',str(rando_id))
        
        #get recipe details
        details = utils.get_recipe_details(rando_id)
        
        details_py = details.json()
        
        if rando:
            rando = rando.text
            details = details.text

    context = {
        'list_of_cuisines': list_of_cuisines,
        'random_recipe': rando,
        'recipe_details': details,
    }

    return render(request, 'pages/test.html', context)



def save_recipe(request,recipe_id):
    if SavedRecipe.objects.filter(user=request.user, recipe_id=recipe_id).exists():
        return redirect(request.META.get('HTTP_REFERER', '/'))
    else:
        details = utils.get_recipe_details(recipe_id).json()
        SavedRecipe.objects.create(
            user=request.user,
            recipe_id=recipe_id,
            recipe_title = details['title'],
            recipe_link = details['sourceUrl'],
            )

    return redirect(request.META.get('HTTP_REFERER', '/'))





