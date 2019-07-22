from django.shortcuts import render
from django import forms
from .models import Cuisine
from . import utils
from . import tests

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
def index(request, id=0):
    
       
    #list of cuisines
    list_of_cuisines = Cuisine.objects.order_by('name')
    selected_cuisine = None
    rando_py = None
    
    #if a cuisine is provided get 
    if id > 0:
        selected_cuisine = Cuisine.objects.get(id=id)
        
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

def recipe(request, id=0):
    details_py = None
    
    if id > 0:
        #get recipe details
        details = utils.get_recipe_details(id)
        
        details_py = details.json()
    
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
    summary = None
    details= None
    
    #Get list of cuisines from database since no way to dynamically pull from spoonful API and no need since will change very rarely
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
        
        #get recipe summary
        summary = utils.get_recipe_summary(rando_id)
        
        summary_py = summary.json()
        
        #get recipe details
        details = utils.get_recipe_details(rando_id)
        
        details_py = details.json()

    context = {
        'list_of_cuisines': list_of_cuisines,
        'random_recipe': rando.text,
        'recipe_summary': summary.text, 
        'recipe_details': details.text,
    }

    return render(request, 'pages/test.html', context)

def about(request):
    context = {
    }

    return render(request, 'pages/about.html', context)








