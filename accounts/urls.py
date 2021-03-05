from django.urls import path
from . import views
urlpatterns = [
     path('logout',views.logoutView,name='logout'),
    path('login',views.loginView,name='login'),
    path('signup',views.signupView,name='signup'),
    path('subscribe',views.subscribeView,name='subscribe'),
    path('contact',views.contactView,name='contact'),
    path('about',views.aboutView,name='about')
]