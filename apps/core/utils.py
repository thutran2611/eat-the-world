import requests
import random
import os

######pull together basic API parameters

#get API key
spoonacular_api_key = os.environ["SPOONACULAR_API_KEY"]
print('Spoonacular API key ->', spoonacular_api_key)

#define required API headers
api_headers = {
"X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
"X-RapidAPI-Key": spoonacular_api_key,
}
print('api_headers ->', api_headers)

#base api url that is decorated with each call
base_api_url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/"
print('base_api_url ->', base_api_url)

######api call functions

#find a random recipe by cuisine among the top 20 rated
def get_recipe_by_cuisine(cuisine):
    print('call to get_recipe_by_cuisine for cuisine ->', cuisine)
    
    #build query string
    base_url = base_api_url + "searchComplex"
    query_params = {
            'cuisine': cuisine,
            'type': 'main course',
            #2 is by "relevance" which I think behaves as ranking it by a score
            'ranking': 2,
            'limitLicense': 'false',
            #to avoid always bringing back the same #1 recipe, randomly select from top 20 ranked recipes returned
            'offset': random.randint(1,21),
            'number': 1,
    }
    
    #build query and make GET request
    response = requests.get(base_url, params=query_params, headers=api_headers)
    
    data = response.json()
    
    return data

#get a summary of the recipe by id
def get_recipe_summary(id):
    print('call to get_recipe_summary for recipe id',str(id))
    
    #build query
    base_url = base_api_url + str(id) + '/summary'
    
    #build query and make GET request
    response = requests.get(base_url, headers=api_headers)

    data = response.json()

    return data
    
#get recipe details by id
def get_recipe_details(id):
    print('call to get_recipe_details for recipe id',str(id))
    
    #build query
    base_url = base_api_url + str(id) + '/information'
    
    #build query and make GET request
    response = requests.get(base_url, headers=api_headers)
    
    data = response.json()
    
    return data
    
    
