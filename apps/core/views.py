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
def index(request):
#    if request.method == 'POST':
#        form = CuisineForm(request.POST)
    context = {}
    return render(request,'pages/index.html',context)

def recipe(request):
    context = {}
    return render(request,'pages/recipe.html',context)


# Two example views. Change or delete as necessary.
def home(request):
    print('home request')
    
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
        rando_id = rando["results"][0]["id"]
        print('rando recipe ID is ->',str(rando_id))
        
        summary = utils.get_recipe_summary(rando_id)
        details = utils.get_recipe_details(rando_id)

    context = {
        'list_of_cuisines': list_of_cuisines,
        'random_recipe': rando,
        'recipe_summary': summary, 
        'recipe_details': details,
    }

    return render(request, 'pages/home.html', context)

def about(request):
    context = {
    }

    return render(request, 'pages/about.html', context)

# test view function
# using placeholder values from the API call to test
# how to retrieve and display specific data
def test_page(request):

    # AT - I moved this data to tests.py since my weak ass computer couldn't process all the brackets in the recipe details which made this file unusable for me.
    rando = tests.rando
    summary = tests.summary
    details = tests.details
    
    context = {
        'random_recipe': rando,
        'recipe_summary': summary, 
        'recipe_details': details,
    }

    return render(request, 'pages/home.html', context)







