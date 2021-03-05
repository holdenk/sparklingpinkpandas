from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from accounts.forms import SignUpForm
from .forms import *
import datetime
from .models import *
from gallery.models import Album
from event.models import Event
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponseRedirect,JsonResponse
# Create your views here.


def homeView(request):
    events = Event.objects.all().order_by('-id')[:3]
    login_form = AuthenticationForm()
    signup_form = SignUpForm()
    posts = Post.objects.all().order_by('-id')[:6]
    latest_posts = Post.objects.all().order_by('-id')[:4]
    albums = Album.objects.all().order_by('-id')[:9]
    context={
        'posts':posts,
        'latest_posts':latest_posts,
        'login_form':login_form,
        'signup_form':signup_form,
        'albums':albums,
        'events':events,
    }
    return render(request,'index.html',context)

def blogListingView(request):
    login_form = AuthenticationForm()
    signup_form = SignUpForm()
    posts = Post.objects.all().order_by('-id')
    latest_posts = Post.objects.all().order_by('-id')[:4]
    if request.method == 'POST':
        q = request.POST.get('q')
        posts = Post.objects.filter(
            Q(title__icontains=q) | Q(description__icontains=q)
        )
    page = request.GET.get('page', 1)
    paginator = Paginator(posts,1) # no of rows to be displayed 
    try:
        postss = paginator.page(page)
    except PageNotAnInteger:
        postss = paginator.page(1)
    except EmptyPage:
        serverss = paginator.page(paginator.num_pages)
    albums = Album.objects.all().order_by('-id')[:9]
    context={
        'posts':posts,
        'latest_posts':latest_posts,
        'albums':albums,
        'login_form':login_form,
        'signup_form':signup_form,
    }
    return render(request,'blog.html',context)

def blogView(request,id):
    post = Post.objects.get(id=id)
    latest_posts = Post.objects.all().order_by('-id')[:4]
    albums = Album.objects.all().order_by('-id')[:9]
    login_form = AuthenticationForm()
    signup_form = SignUpForm()
    context={
        'post':post,
        'latest_posts':latest_posts,
        'albums':albums,
        'login_form':login_form,
        'signup_form':signup_form,
    }
    return render(request,'single-post.html',context)




def blogLike(request):
    id = request.GET.get('id')
    article = Post.objects.get(id=id)
    user = request.user
    if user in article.liker.all():
        article.liker.remove(user)
        article.like_count = article.like_count - 1
    else:
        article.liker.add(user)
        article.like_count = article.like_count + 1
    article.save()
    data = {
        'like_no':article.like_count,
    }
    return JsonResponse(data)

def blogComment(request):
    id = request.GET.get('id')
    article = Post.objects.get(id=id)
    user = request.user
    comment = Coment(
            user = user,
            comment_text = request.GET.get('comment_text'),
        )
    comment.save()
    article.coments.add(comment)
    article.comment_count = article.comment_count + 1
    article.save()
    data = {
        'comment_no':article.comment_count,
    }
    return JsonResponse(data)

def blogCommentReply(request):
    id = request.GET.get('id')
    comment_id = request.GET.get('comment_id')
    article = Post.objects.get(id=id)
    comment = Coment.objects.get(id=comment_id)
    user = request.user
    reply = Rply(
            user = user,
            reply_text = request.GET.get('reply_text'),
        )
    reply.save()
    comment.rplies.add(reply)
    article.comment_count = article.comment_count + 1
    article.save()
    comment.save()
    data = {
        'comment_no':article.comment_count,
    }
    return JsonResponse(data)

