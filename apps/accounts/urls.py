from django.urls import path

from apps.accounts import views

urlpatterns = [
    path('login/', views.log_in, name='login'),
    path('signup/', views.signup, name ='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('users/<username>/', views.view_profile, name='view_profile'),
#    path('users/', views.view_all_users, name='view_all_users'),
#    path('account/', views.account_view, name ='account'),

]
