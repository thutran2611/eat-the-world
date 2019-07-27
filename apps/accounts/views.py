from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from apps.accounts.forms import UserEditForm, SignupForm
from apps.accounts.models import User
from apps.core.models import SavedRecipe

#sign up
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Log-in the user right away
            messages.success(request, 'Account created successfully. Welcome!')
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

#login
def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('view_profile', user.username)
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

#logout
def logout_view(request):
    logout(request)
    messages.success(request, 'Signed out.')
    return redirect('index')
    
#view profile page
@login_required(login_url='login')
def view_profile(request, username):
    user = User.objects.get(username=username)

    if request.user == user:
        is_viewing_self = True
    else:
        is_viewing_self = False

    saved_recipes = SavedRecipe.objects.order_by('-created')
    saved_by_user = saved_recipes.filter(user=user)
    context = {
        'user': user,
        'is_viewing_self': is_viewing_self,
        'saved_recipes':saved_by_user,
    }
    return render(request, 'accounts/user_account.html', context)


#edit profile
@login_required(login_url='login')
def edit_profile(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserEditForm(instance=request.user)

    context = {
        'form': form,
    }
    return render(request, 'accounts/edit_profile.html', context)


#def account_view(request):
#    context =  {}
#    return render(request, 'accounts/user_account.html', context)


    
#def view_all_users(request):
#    all_users = User.objects.all()
#    context = {
#        'users': all_users,
#    }
#    return render(request, 'accounts/view_all_users.html', context)




