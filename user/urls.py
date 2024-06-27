from django.urls import path
from user.views import user_list,create_user, login_user,home

urlpatterns = [
    path('',user_list,name="user-list"),
    path('create',create_user,name="user-create"),
    path('login_user',login_user,name='login'),
    path('home',home,name="home")

]