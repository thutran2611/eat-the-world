from django.shortcuts import render, redirect
from django import forms
from .models import Cuisine, SavedRecipe
from . import utils
from . import tests
from apps.accounts.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

class CuisineForm(forms.Form):
    cuisine = forms.ModelChoiceField(queryset=Cuisine.objects.order_by('name'))
    
class SavedRecipeForm(forms.Form):
    recipe_id = forms.IntegerField(widget=forms.HiddenInput())
    title = forms.CharField(widget=forms.HiddenInput())

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
    form = None
    
    if recipe_id > 0:
        #get recipe details
        details = utils.get_recipe_details(recipe_id)
        
        details_py = details.json()
        
        default_form_data = {
                    'recipe_id': recipe_id,
                    'title': details_py['title'],
        }
        form = SavedRecipeForm(default_form_data)
    else:
        print('Call to get recipe details without a recipe id')
        print(request)
    
    context = {
        "recipe": details_py,
        "form": form,
        
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


@login_required()
def save_recipe(request):
    print(request.POST)
#    if request.user.is_authenticated:
    is_already_saved = SavedRecipe.objects.filter(recipe_id=request.POST['recipe_id'],
        user=request.user,
    )
    if not is_already_saved:
        SavedRecipe.objects.create(
           user=request.user,
           recipe_id=request.POST['recipe_id'],
           title=request.POST['title'],
        )
    else:
        print('recipe already saved by this user')
#    else:
#        print('Unauthenticated user attempted to save a favorite')

    return redirect(request.META.get('HTTP_REFERER', '/'))



