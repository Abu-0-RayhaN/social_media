from django.shortcuts import redirect, render,HttpResponseRedirect
from.forms import CreateUserForm,EditProfileForm
from .models import UserProfile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required

def sign_up(request):
    form=CreateUserForm()
    registered=False
    if request.method=='POST':
        form=CreateUserForm(data=request.POST)
        if form.is_valid():
            user= form.save()
            registered=True
            user_profile = UserProfile(user=user)
            user_profile.save()
            return redirect('App_login:authlogin')

    return render(request,'App_login/signup.html',context={'title':'Sign Up. Intagram','form':form})
def authlogin(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('profile'))

    return render(request, 'App_Login/login.html', context={'title':'Login . Social','form':form})
@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_login:authlogin'))
@login_required
def editprofile(request):
    current = UserProfile.objects.get(user=request.user)
    form = EditProfileForm(instance=current)
    if request.method =="POST":
        form=EditProfileForm(request.POST,request.FILES,instance=current)
        if form.is_valid():
            form.save(commit=True)
            form =EditProfileForm(instance=current)
            return redirect('profile')
    return render(request,'App_login/editprofile.html',context={'form':form,'title':'Edit Profile.social'})

