from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from.forms import CreateUserForm, UserUpdateForm, ProfileUpdateFrom

# Create your views here.

def register(request):
    if request.method =="POST":  
        form= CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return render('user-login')
    else:
        form =CreateUserForm()
    context= {
        'form':form,
    }
    return render(request,'user/register.html',context)

def profile(request):
    return render(request,'user/profile.html')

def profile_update(request):
    if request.method=="POST":
        user_form =UserUpdateForm(request.POST,)
        profile_form = ProfileUpdateFrom(request.POST,request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return render('user-profile')
    else:
        user_form = user_form =UserUpdateForm(instance=request.user)
        profile_form=ProfileUpdateFrom(instance=request.user.profile)
    context={
        'user_form':user_form,
        'profile_form':profile_form
    }
    return render(request,'user/profile_update.html',context)