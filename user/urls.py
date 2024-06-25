from django.urls import path
from user.views import user_list, create_user, login_user

urlpatterns = [
    path('', user_list, name="user-list"),
    path('create', create_user, name="create-user"),
    path('login_user', login_user, name= 'login') 
]