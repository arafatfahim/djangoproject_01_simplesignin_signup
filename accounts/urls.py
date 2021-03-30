from django.urls import path
from django.conf.urls import url
from .views import login, register, logout, profile

##app_name = 'accounts'
urlpatterns = [
    path('register/', register, name="register"),
    path('login/', login, name="login"),
    path('logout/', logout,name="logout"),
    path('profile/', profile,name="profile"),
    ]
