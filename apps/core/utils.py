import requests
import random
import os

###### pull together basic API parameters

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

#variable to hold api limits
api_limit_stats = {}

###### api call functions

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
            'instructionsRequired': 'true',
            'limitLicense': 'false',
            #to avoid always bringing back the same #1 recipe, randomly select from top 20 ranked recipes returned
            'offset': random.randint(1,21),
            'number': 1,
    }
    
    #build query and make GET request
    response = requests.get(base_url, params=query_params, headers=api_headers)
    
    process_response_headers(response.headers)
    
    return response

#get recipe details by id
def get_recipe_details(id):
    print('call to get_recipe_details for recipe id',str(id))
    
    #build query
    base_url = base_api_url + str(id) + '/information'
    
    #build query and make GET request
    response = requests.get(base_url, headers=api_headers)
    
    process_response_headers(response.headers)
    
    return response
    
#check response headers for nearing api limit
def process_response_headers(header_dict):
    for header_key, header_value in header_dict.items():
        if 'X-RateLimit' in header_key:
            api_limit_stats[header_key] = header_value
        
    print('api_limit_stats ->', api_limit_stats)
    
    if int(api_limit_stats['X-RateLimit-requests-Remaining']) < 4900 or int(api_limit_stats['X-RateLimit-results-Remaining']) < 19900:
        msg = "You are getting close to exceeding one or more Spoonacular API limits. The remaining capacity before getting charged is : \n" + "X-RateLimit-requests-Remaining : " + api_limit_stats['X-RateLimit-requests-Remaining'] + "\n" + "X-RateLimit-results-Remaining : " + api_limit_stats['X-RateLimit-results-Remaining'] + "\n" + "IT STARTS COSTING $$$ IF WE EXCEED LIMITS, INSTEAD OF JUST THROWING AN ERROR!!!"
        print ('API getting close to limits!')
        send_email(msg)
    
#send email
def send_email(message):

    #send email using mailgun API
    mailgun_api_key = os.environ["MAILGUN_API_KEY"]
    
    print(mailgun_api_key)

    r = requests.post(
        "https://api.mailgun.net/v3/sandboxb364b46bb57a4f7bb415814c33300234.mailgun.org/messages",
        auth=("api", mailgun_api_key),
        data={"from": "API Counter <api_counter@eat-the-world.com>",
            "to": "API Check <api_check@awjdthornton.com>",
            "subject": "API Calls Near Limit!",
            "text": message}
    )
    
    print('send email mailgun post status_code =>',r.status_code)
    
    #for testing purposes
    return r.status_code





