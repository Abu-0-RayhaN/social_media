from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from App_login.models import UserProfile
from .models import Posts,Follow,Like
from django.urls import reverse
from .forms import PostForm
from django.contrib.auth.models import User
def home(request):
    following_list = Follow.objects.filter(follower=request.user)
    posts=Posts.objects.filter(author__in=following_list.values_list('following'))
    liked_post=Like.objects.filter(user=request.user)
    liked_post_list=liked_post.values_list('post',flat=True)
    print(liked_post)
    if request.method == "GET":
        search= request.GET.get('search',' ')
        result = User.objects.filter(username__icontains=search)#i am using this contains key to get related name user.
        
    return render(request,'index.html',context={'result':result,'search':search,'following_list':following_list,'posts':posts,'like_post':liked_post_list})

@login_required
def profile(request):
    current = UserProfile.objects.get(user=request.user)
    form = PostForm()
    if request.method=="POST":
        form= PostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('/')
    return render(request,'App_login/profile.html',context={'profile':current,'form':form})
@login_required

def seeUserProfile(request,username):
    user= User.objects.get(username=username)
    already_followed = Follow.objects.filter(follower=request.user,following=user)
    print(already_followed)
    if user == request.user:
        return redirect('profile')
    return render(request,'App_post/view_profile.html',context={'user':user,'already_followed':already_followed})
@login_required

def follow(request,username):
    following_user = User.objects.get(username=username)
    print(following_user)
    follower_user = request.user
    print(follower_user)
    already_followed = Follow.objects.filter(follower=follower_user, following=following_user)
    print(already_followed)
    if not already_followed:
        followed_user = Follow(follower=follower_user,following=following_user)
        followed_user.save()
        return HttpResponseRedirect(reverse('viewprofile',kwargs={'username':username}))
    
@login_required

def unfollow(request,username):
    following_user=User.objects.get(username=username)
    follower_user=request.user
    already_followed= Follow.objects.filter(follower=follower_user,following=following_user)
    already_followed.delete()
    return HttpResponseRedirect(reverse('viewprofile',kwargs={'username':username}))

@login_required 
def liked(request,pk):
    post= Posts.objects.get(pk=pk)
    already_liked=Like.objects.filter(post=post,user=request.user)
    if not already_liked:
        liked_post=Like(post=post,user=request.user)
        liked_post.save()
        return HttpResponseRedirect(reverse('home'))
@login_required

def Unilked(request,pk):
    post= Posts.objects.get(pk=pk)
    already_liked=Like.objects.filter(post=post,user=request.user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('home'))

    
