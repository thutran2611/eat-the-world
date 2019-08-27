import requests
import random
import os

###### pull together basic API parameters

#get API keys
if os.environ["SPOONACULAR_API_KEY"]:
  spoonacular_api_key = os.environ["SPOONACULAR_API_KEY"]
  print('Spoonacular API key ->', spoonacular_api_key)
else:
  print('Missing Spoonacular API key')


if os.environ["MAILGUN_API_KEY"]:
  mailgun_api_key = os.environ["MAILGUN_API_KEY"]
  print(mailgun_api_key)
else:
  print('Missing Mailgun API key')
  
#base api url that is decorated with each call
base_api_url = "https://api.spoonacular.com/recipes/"
print('base_api_url ->', base_api_url)


#variable to hold api limits
api_limit_stats = {}

###### api call functions

#find a random recipe by cuisine among the top 20 rated
def get_recipe_by_cuisine(cuisine):
    print('call to get_recipe_by_cuisine for cuisine ->', cuisine)
    
    #build query string
    base_url = base_api_url + "searchComplex" + '?apiKey=' + spoonacular_api_key
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
    
    url_params = ''
    for key, value in query_params.items():
      url_params += '&' + key + '=' + str(value)
      
    url = base_url + url_params
    print('url ->', url)
    
    #build query and make GET request
    response = requests.get(url)
    
    if response.status_code == 200:
      process_response_headers(response.headers)
    
    #TODO only return response if 200. Otherwise through 500 error
    return response

#get recipe details by id
def get_recipe_details(id):
    print('call to get_recipe_details for recipe id',str(id))
    
    #build query
    url = base_api_url + str(id) + '/information' + '?apiKey=' + spoonacular_api_key
    
    #build query and make GET request
    response = requests.get(url)
    
    if response.status_code == 200:
      process_response_headers(response.headers)
    
    #TODO only return response if 200. Otherwise through 500 error
    return response
    
#check response headers for nearing api limit
def process_response_headers(header_dict):
    print('header_dict ->', header_dict)
    for header_key, header_value in header_dict.items():
        if 'X-API-Quota' in header_key:
            api_limit_stats[header_key] = header_value
        
    print('api_limit_stats ->', api_limit_stats)
    
    if float(api_limit_stats['X-API-Quota-Used']) > 125:
        msg = "You are getting close to exceeding the daily Spoonacular API limits of 150 points. If calls exceed 150 points then 402 error will be returned"
        print ('API getting close to limits!')
        send_email(msg)
    
#send email
def send_email(message):

    #send email using mailgun API

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





