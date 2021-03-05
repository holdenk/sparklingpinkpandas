from django.urls import path
from . import views
urlpatterns = [
    path('',views.eventView,name='event'),
    path('addEvent',views.addEventView,name='addevent')
]