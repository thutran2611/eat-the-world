from django.shortcuts import render
from django import forms
from . import utils

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

# test view function
# using placeholder values from the API call to test
# how to retrieve and display specific data
def test_page(request):
    rando = {'results': [{'id': 668772, 'title': 'Classic Bacon and Cheese burger', 'image': 'https://spoonacular.com/recipeImages/668772-312x231.jpg', 'imageType': 'jpg'}], 'baseUri': 'https://spoonacular.com/recipeImages/', 'offset': 15, 'number': 1, 'totalResults': 24231, 'processingTimeMs': 261}
    summary = {'id': 482574, 'title': 'Slow Cooker Vegetarian Chili with Butternut Squash', 'summary': 'Slow Cooker Vegetarian Chili with Butternut Squash might be a good recipe to expand your main course recipe box. One serving contains <b>314 calories</b>, <b>16g of protein</b>, and <b>3g of fat</b>. This gluten free, dairy free, and lacto ovo vegetarian recipe serves 4 and costs <b>$2.38 per serving</b>. 3278 people found this recipe to be delicious and satisfying. This recipe is typical of American cuisine. It will be a hit at your <b>The Super Bowl</b> event. If you have butternut squash, oregano, fire roasted tomatoes, and a few other ingredients on hand, you can make it. From preparation to the plate, this recipe takes about <b>4 hours and 10 minutes</b>. It is brought to you by The Lemon Bowl. Taking all factors into account, this recipe <b>earns a spoonacular score of 100%</b>, which is super. If you like this recipe, you might also like recipes such as <a href="https://spoonacular.com/recipes/slow-cooker-butternut-squash-chili-944925">Slow Cooker Butternut Squash Chili</a>, <a href="https://spoonacular.com/recipes/slow-cooker-butternut-squash-chili-943952">Slow Cooker Butternut Squash Chili</a>, and <a href="https://spoonacular.com/recipes/slow-cooker-butternut-squash-and-quinoa-chili-713244">Slow Cooker Butternut Squash and Quinoa Chili</a>.'}
    details = {'vegetarian': True, 'vegan': False, 'glutenFree': True, 'dairyFree': True, 'veryHealthy': True, 'cheap': False, 'veryPopular': True, 'sustainable': False, 'weightWatcherSmartPoints': 5, 'gaps': 'no', 'lowFodmap': False, 'ketogenic': False, 'whole30': False, 'preparationMinutes': 10, 'cookingMinutes': 240, 'sourceUrl': 'http://thelemonbowl.com/2013/04/slow-cooker-vegetarian-chili-with-butternut-squash.html', 'spoonacularSourceUrl': 'https://spoonacular.com/slow-cooker-vegetarian-chili-with-butternut-squash-482574', 'aggregateLikes': 3278, 'spoonacularScore': 100.0, 'healthScore': 86.0, 'creditsText': 'The Lemon Bowl', 'sourceName': 'The Lemon Bowl', 'pricePerServing': 237.99, 'extendedIngredients': [{'id': 11485, 'aisle': 'Produce', 'image': 'butternut-squash.jpg', 'consitency': 'solid', 'name': 'butternut squash', 'original': '4 cups butternut squash - peeled and diced', 'originalString': '4 cups butternut squash - peeled and diced', 'originalName': 'butternut squash - peeled and diced', 'amount': 4.0, 'unit': 'cups', 'meta': ['diced', 'peeled'], 'metaInformation': ['diced', 'peeled'], 'measures': {'us': {'amount': 4.0, 'unitShort': 'cups', 'unitLong': 'cups'}, 'metric': {'amount': 946.352, 'unitShort': 'ml', 'unitLong': 'milliliters'}}}, {'id': 2009, 'aisle': 'Spices and Seasonings', 'image': 'chili-powder.jpg', 'consitency': 'solid', 'name': 'chili powder', 'original': '1 tablespoon chili powder', 'originalString': '1 tablespoon chili powder', 'originalName': 'chili powder', 'amount': 1.0, 'unit': 'tablespoon', 'meta': [], 'metaInformation': [], 'measures': {'us': {'amount': 1.0, 'unitShort': 'Tbsp', 'unitLong': 'Tbsp'}, 'metric': {'amount': 1.0, 'unitShort': 'Tbsp', 'unitLong': 'Tbsp'}}}, {'id': 99223, 'aisle': 'Canned and Jarred;Ethnic Foods', 'image': 'canned-chipotle.png', 'consitency': 'solid', 'name': 'chipotle peppers in adobo', 'original': '2 chipotle peppers in adobo - minced (remove seeds to lower heat)', 'originalString': '2 chipotle peppers in adobo - minced (remove seeds to lower heat)', 'originalName': 'chipotle peppers in adobo - minced (remove seeds to lower heat)', 'amount': 2.0, 'unit': '', 'meta': ['minced', '(remove seeds to lower heat)'], 'metaInformation': ['minced', '(remove seeds to lower heat)'], 'measures': {'us': {'amount': 2.0, 'unitShort': '', 'unitLong': ''}, 'metric': {'amount': 2.0, 'unitShort': '', 'unitLong': ''}}}, {'id': 1002014, 'aisle': 'Spices and Seasonings', 'image': 'ground-cumin.jpg', 'consitency': 'solid', 'name': 'cumin', 'original': '2 tablespoons cumin', 'originalString': '2 tablespoons cumin', 'originalName': 'cumin', 'amount': 2.0, 'unit': 'tablespoons', 'meta': [], 'metaInformation': [], 'measures': {'us': {'amount': 2.0, 'unitShort': 'Tbsps', 'unitLong': 'Tbsps'}, 'metric': {'amount': 2.0, 'unitShort': 'Tbsps', 'unitLong': 'Tbsps'}}}, {'id': 98849, 'aisle': 'Canned and Jarred', 'image': 'tomatoes-canned.png', 'consitency': 'solid', 'name': 'fire roasted tomatoes', 'original': '14 oz fire roasted diced tomatoes', 'originalString': '14 oz fire roasted diced tomatoes', 'originalName': 'fire roasted diced tomatoes', 'amount': 14.0, 'unit': 'oz', 'meta': ['diced', 'fire roasted'], 'metaInformation': ['diced', 'fire roasted'], 'measures': {'us': {'amount': 14.0, 'unitShort': 'oz', 'unitLong': 'ounces'}, 'metric': {'amount': 396.893, 'unitShort': 'g', 'unitLong': 'grams'}}}, {'id': 11167, 'aisle': 'Produce', 'image': 'corn-on-the-cob.jpg', 'consitency': 'solid', 'name': 'fresh corn', 'original': '1 cup corn - fresh or frozen', 'originalString': '1 cup corn - fresh or frozen', 'originalName': 'corn - fresh or frozen', 'amount': 1.0, 'unit': 'cup', 'meta': ['fresh'], 'metaInformation': ['fresh'], 'measures': {'us': {'amount': 1.0, 'unitShort': 'cup', 'unitLong': 'cup'}, 'metric': {'amount': 236.588, 'unitShort': 'ml', 'unitLong': 'milliliters'}}}, {'id': 11215, 'aisle': 'Produce', 'image': 'garlic.jpg', 'consitency': 'solid', 'name': 'garlic', 'original': '3 cloves garlic - minced', 'originalString': '3 cloves garlic - minced', 'originalName': 'garlic - minced', 'amount': 3.0, 'unit': 'cloves', 'meta': ['minced'], 'metaInformation': ['minced'], 'measures': {'us': {'amount': 3.0, 'unitShort': 'cloves', 'unitLong': 'cloves'}, 'metric': {'amount': 3.0, 'unitShort': 'cloves', 'unitLong': 'cloves'}}}, {'id': 16033, 'aisle': 'Pasta and Rice;Canned and Jarred', 'image': 'kidney-beans.jpg', 'consitency': 'solid', 'name': 'kidney beans', 'original': '14 oz kidney beans - drained and rinsed', 'originalString': '14 oz kidney beans - drained and rinsed', 'originalName': 'kidney beans - drained and rinsed', 'amount': 14.0, 'unit': 'oz', 'meta': ['drained and rinsed'], 'metaInformation': ['drained and rinsed'], 'measures': {'us': {'amount': 14.0, 'unitShort': 'oz', 'unitLong': 'ounces'}, 'metric': {'amount': 396.893, 'unitShort': 'g', 'unitLong': 'grams'}}}, {'id': 6970, 'aisle': 'Canned and Jarred', 'image': 'chicken-broth.png', 'consitency': 'liquid', 'name': 'low sodium chicken broth', 'original': '2 cups vegetable or chicken broth - low sodium', 'originalString': '2 cups vegetable or chicken broth - low sodium', 'originalName': 'vegetable or chicken broth - low sodium', 'amount': 2.0, 'unit': 'cups', 'meta': ['low sodium'], 'metaInformation': ['low sodium'], 'measures': {'us': {'amount': 2.0, 'unitShort': 'cups', 'unitLong': 'cups'}, 'metric': {'amount': 473.176, 'unitShort': 'ml', 'unitLong': 'milliliters'}}}, {'id': 11282, 'aisle': 'Produce', 'image': 'brown-onion.png', 'consitency': 'solid', 'name': 'onion', 'original': '1 medium onion - diced', 'originalString': '1 medium onion - diced', 'originalName': 'onion - diced', 'amount': 1.0, 'unit': 'medium', 'meta': ['diced'], 'metaInformation': ['diced'], 'measures': {'us': {'amount': 1.0, 'unitShort': 'medium', 'unitLong': 'medium'}, 'metric': {'amount': 1.0, 'unitShort': 'medium', 'unitLong': 'medium'}}}, {'id': 2027, 'aisle': 'Produce;Spices and Seasonings', 'image': 'oregano.jpg', 'consitency': 'solid', 'name': 'oregano', 'original': '1 teaspoon oregano', 'originalString': '1 teaspoon oregano', 'originalName': 'oregano', 'amount': 1.0, 'unit': 'teaspoon', 'meta': [], 'metaInformation': [], 'measures': {'us': {'amount': 1.0, 'unitShort': 'tsp', 'unitLong': 'teaspoon'}, 'metric': {'amount': 1.0, 'unitShort': 'tsp', 'unitLong': 'teaspoon'}}}, {'id': 11821, 'aisle': 'Produce', 'image': 'red-pepper.jpg', 'consitency': 'solid', 'name': 'red bell pepper', 'original': '1 red pepper - seeded and diced', 'originalString': '1 red pepper - seeded and diced', 'originalName': 'red pepper - seeded and diced', 'amount': 1.0, 'unit': '', 'meta': ['diced', 'red', 'seeded'], 'metaInformation': ['diced', 'red', 'seeded'], 'measures': {'us': {'amount': 1.0, 'unitShort': '', 'unitLong': ''}, 'metric': {'amount': 1.0, 'unitShort': '', 'unitLong': ''}}}, {'id': 1102047, 'aisle': 'Spices and Seasonings', 'image': 'salt-and-pepper.jpg', 'consitency': 'solid', 'name': 'salt and pepper', 'original': 'salt and pepper to taste', 'originalString': 'salt and pepper to taste', 'originalName': 'salt and pepper to taste', 'amount': 4.0, 'unit': 'servings', 'meta': ['to taste'], 'metaInformation': ['to taste'], 'measures': {'us': {'amount': 4.0, 'unitShort': 'servings', 'unitLong': 'servings'}, 'metric': {'amount': 4.0, 'unitShort': 'servings', 'unitLong': 'servings'}}}, {'id': 1012028, 'aisle': 'Spices and Seasonings', 'image': 'paprika.jpg', 'consitency': 'solid', 'name': 'smoked paprika', 'original': '1 tablespoon smoked paprika', 'originalString': '1 tablespoon smoked paprika', 'originalName': 'smoked paprika', 'amount': 1.0, 'unit': 'tablespoon', 'meta': ['smoked'], 'metaInformation': ['smoked'], 'measures': {'us': {'amount': 1.0, 'unitShort': 'Tbsp', 'unitLong': 'Tbsp'}, 'metric': {'amount': 1.0, 'unitShort': 'Tbsp', 'unitLong': 'Tbsp'}}}], 'id': 482574, 'title': 'Slow Cooker Vegetarian Chili with Butternut Squash', 'readyInMinutes': 250, 'servings': 4, 'image': 'https://spoonacular.com/recipeImages/482574-556x370.jpg', 'imageType': 'jpg', 'cuisines': ['american'], 'dishTypes': ['lunch', 'main course', 'main dish', 'dinner'], 'diets': ['gluten free', 'dairy free', 'lacto ovo vegetarian'], 'occasions': ['super bowl'], 'winePairing': {'pairedWines': ['cava', 'grenache', 'shiraz'], 'pairingText': "Chili on the menu? Try pairing with Cava, Grenache, and Shiraz. These juicy reds don't have too much tannin (important for spicy foods), but a sparkling wine like cava can tame the heat even better. You could try Juve Y Camps Brut Nature Reserva de la Familia Cava. Reviewers quite like it with a 4.3 out of 5 star rating and a price of about 16 dollars per bottle.", 'productMatches': [{'id': 433977, 'title': 'Juve Y Camps Brut Nature Reserva de la Familia Cava', 'description': 'Pale gold in color, this Cava has aromas of mature white peach, toasted bread and green tea with hints of lemon citrus and apricots. Equally rich and broad on the palate, these flavors continue to unfold on the palate.Its fresh profile makes it a perfect match for pate, seafood, tapas, paellas, grilled poultry or cured meats.', 'price': '$15.99', 'imageUrl': 'https://spoonacular.com/productImages/433977-312x231.jpg', 'averageRating': 0.86, 'ratingCount': 10.0, 'score': 0.827741935483871, 'link': 'https://click.linksynergy.com/deeplink?id=*QCiIS6t4gA&mid=2025&murl=https%3A%2F%2Fwww.wine.com%2Fproduct%2Fjuve-y-camps-brut-nature-reserva-de-la-familia-cava-2011%2F150306'}]}, 'instructions': 'Place all ingredients in your slow cooker and heat on High for 4 hours or Low for 8 hours.Garnish with scallions, Greek yogurt, cilantro or crushed tortilla chips.', 'analyzedInstructions': [{'name': '', 'steps': [{'number': 1, 'step': 'Place all ingredients in your slow cooker and heat on High for 4 hours or Low for 8 hours.', 'ingredients': [], 'equipment': [{'id': 404718, 'name': 'slow cooker', 'image': 'slow-cooker.jpg'}]}, {'number': 2, 'step': 'Garnish with scallions, Greek yogurt, cilantro or crushed tortilla chips.', 'ingredients': [], 'equipment': []}]}]}
    context = {
        'random_recipe': rando,
        'recipe_summary': summary, 
        'recipe_details': details,
    }

    return render(request, 'pages/home.html', context)





