from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import SignUpForm
import datetime
from .models import *
from django.http import HttpResponseRedirect,JsonResponse

from django.core.mail import send_mail, BadHeaderError, EmailMultiAlternatives
# Create your views here.
def homePageView(request):
    return render(request,'index.html',{})

def loginView(request):
    login_form = AuthenticationForm()
    error = None
    print('test')
    if request.method == 'POST':
        print('post')
        login_form = AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if request.POST.get('page') == 'booking':
                    return redirect('/beauty_spa/booking')
                elif request.POST.get('page') == 'mybookings':
                    return redirect('/beauty_spa/mybookings')
                else:
                    return JsonResponse({})
            else:
                error = "Invalid username or password."
        else:
            error = "Invalid username or password."  
        return JsonResponse(data={'error':error})
    return render(request, 'accounts/login.html', {'login_form':login_form,'error':error,'page':'accounts'})

def signupView(request):
    signup_form = SignUpForm()
    error = None
    print('test')
    if request.method == 'POST':
        print('test2')
        signup_form = SignUpForm(request.POST)
        try:
            User.objects.get(email=request.POST.get('email'))
            email_error = 'Email already exist'
            print('testemail')
        except:
            email_error = ''
        if signup_form.is_valid():
                print('test3')
                signup_form.save()
                username = signup_form.cleaned_data.get('username')
                raw_password = signup_form.cleaned_data.get('password1')
                
                user = authenticate(username=username, password=raw_password)
                user_details = User_Details(
                    user = user
                )
                user_details.save()
                login(request, user)
                return JsonResponse({})
        try:
            errors = signup_form.errors['username'].as_data() 
            for error in errors:
                username_error = 'username already exists'
        except:
            username_error = ''
        try:
            errors = signup_form.errors['password2'].as_data() 
            print(errors)
            for error in signup_form.errors['password2'].as_data() :
                for e in error:
                    print(e)
                pass_error = e
                print(error)
        except:
            pass_error = ''
            print('test')
        
        data = {
            'email_error':email_error,
            'username_error':username_error,
            'password_error':pass_error,
            'error':'True',
        }
        return JsonResponse(data)
    return render(request, 'accounts/signup.html', {'signup_form':signup_form,'page':'accounts'})

def logoutView(request):
    logout(request)
    return redirect('/')

def subscribeView(request):
    e_mail=request.GET.get("email")
    try:
        print(e_mail)
        email = Mailing.objects.get(email=e_mail)
        print(e_mail)
    except:
        email = Mailing(
            email=e_mail,
        )
        email.save() 
    return JsonResponse({})

def contactView(request):
    login_form = AuthenticationForm()
    signup_form = SignUpForm()
    if request.method == 'POST':
        subject = f'Message from {request.POST.get("name")} with email: {request.POST.get("email")}'
        from_email, to =  'sparklingspinkpandas@gmail.com', 'sparklingspinkpandas@gmail.com'
        text_content = request.POST.get('message')
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.send()
    context={
        'login_form':login_form,
        'signup_form':signup_form,
    }
    return render(request,'contact.html',context)

def aboutView(request):
    login_form = AuthenticationForm()
    signup_form = SignUpForm()
    context={
        'login_form':login_form,
        'signup_form':signup_form,
    }
    return render(request,'about.html',context)