from django.shortcuts import render
from django import forms
from . import utils

# Two example views. Change or delete as necessary.
def home(request):
    #Get list of cuisines from database since no way to dynamically pull from spoonful API and no need since will change very rarely
    
    # TODO get list of cuisines from database

    data=''
    cuisines=''
    rando=''
    summary=''
    details=''
    
    # TODO figure out how request will be coming in for a recipe
    #Get 1 recipe if request includes a cuisine
#    if request.method == 'GET' and request.GET['cuisine']:
#        data = utils.get_recipe_by_cuisine(request.GET['cuisine'])
        
    #temporary call to each api query function
    rando = utils.get_recipe_by_cuisine('american')
    summary = utils.get_recipe_summary(482574)
    details = utils.get_recipe_details(482574)

    context = {
        'list_of_cusines': cuisines,
        'random_recipe': rando,
        'recipe_summary': summary, 
        'recipe_details': details,
    }

    return render(request, 'pages/home.html', context)

def about(request):
    context = {
    }

    return render(request, 'pages/about.html', context)

