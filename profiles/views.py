from django.shortcuts import render, redirect
from .models import profile
from django.contrib import messages

# Create your views here.

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
