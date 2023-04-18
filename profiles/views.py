from django.shortcuts import render, redirect
from .models import profile
from django.contrib import messages

# Create your views here.

def home(request):
    profiles = profile.objects.all()
    ctx = {'profiles': profiles}
    return render(request, 'profiles/home.html', ctx)


def profile(request):
    # add person form
    form = profile(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save() # save the form data to model
            messages.success(request, 'Your details added successfully')
            return redirect('profile')
        else:
            messages.error(request, 'Error adding your details')
    ctx = {'form': form}
    return render(request, 'profiles/profile.html', ctx)

def add_profile(request):
    # add person form
    form = profile(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save() # save the form data to model
            messages.success(request, 'Your details added successfully')
            return redirect('profile')
        else:
            messages.error(request, 'Error adding your details')
    ctx = {'form': form}
    return render(request, 'profiles/profile.html', ctx)
 
def view_profile(request, id):
    profile = profile.objects.get(id=id)
    ctx = {'profile': profile}
    return render(request, 'profiles/profile.html', ctx)



def edit_profile(request, id):
    profile = profile.objects.get(id=id)
    form = profile(request.POST or None, request.FILES or None, instance=profile)
    if request.method == 'POST':
        if form.is_valid():
            form.save() # save the form data to model
            messages.success(request, 'Your details added successfully')
            return redirect('profile')
        else:
            messages.error(request, 'Error adding your details')
    ctx = {'form': form}
    return render(request, 'profiles/profile.html', ctx)

def delete_profile(request, id):    
    profile = profile.objects.get(id=id)
    profile.delete()
    messages.success(request, 'Your details added successfully')
    return redirect('profile')

