from django.shortcuts import render
from .models import Event
from gallery.models import Album
from blog.models import Post
from .forms import *
from accounts.forms import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.
def eventView(request):
    events = Event.objects.all().order_by('-id')
    latest_posts = Post.objects.all().order_by('-id')[:4]
    albums = Album.objects.all().order_by('-id')[:9]
    login_form = AuthenticationForm()
    signup_form = SignUpForm()
    context={
        'events':events,
        'latest_posts':latest_posts,
        'albums':albums,
        'login_form':login_form,
        'signup_form':signup_form,
    }
    return render(request,'events.html',context)

def addEventView(request):
    form = EventForm()
    login_form = AuthenticationForm()
    signup_form = SignUpForm()
    if request.method == 'POST':
        form = EventForm(request.POST)
        print('test')   
        if form.is_valid(): 
            print('test')   
            post = Event(
                caption = form.cleaned_data['caption'],
                description = form.cleaned_data['description'],
                date = request.POST.get('date'),
            )        
            if request.FILES:
                post.image =   request.FILES['image']           
            post.save()
    context = {
            'form':form,
            'login_form':login_form,
            'signup_form':signup_form,
            }
    return render(request,'add-blog.html',context)