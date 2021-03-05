from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponseRedirect,JsonResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accounts.forms import SignUpForm
# Create your views here.
def galleryView(request):
    albums = Album.objects.all().order_by('-id')
    login_form = AuthenticationForm()
    signup_form = SignUpForm()
    context={
        'albums':albums,
        'login_form':login_form,
        'signup_form':signup_form,
    }
    return render(request,'gallery.html',context)


    
