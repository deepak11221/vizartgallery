from django.shortcuts import render, redirect
from django.contrib import messages
from .models import graph

# Create your views here.

def add_graph(request):
    # add person form
    form = graph(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save() # save the form data to model
            messages.success(request, 'Your details added successfully')
            return redirect('home')
        else:
            messages.error(request, 'Error adding your details')
    ctx = {'form': form}
    return render(request, 'graph/graph.html', ctx)