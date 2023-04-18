from django.shortcuts import render, redirect
from django.contrib import messages
from .models import snippet, category
from .forms import categoryForm, snippetForm
# Create your views here.

def home(request):
    categories = category.objects.all()
    ctx = {'categories': categories}
    return render(request, 'gallery/home.html', ctx)

def add_category(request):
    # add person form
    form = category(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save() # save the form data to model
            messages.success(request, 'Your details added successfully')
            return redirect('home')
        else:
            messages.error(request, 'Error adding your details')
    ctx = {'form': form}
    return render(request, 'gallery/category.html', ctx)

def add_snippet(request):
    # add person form
    form = snippet(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save() # save the form data to model
            messages.success(request, 'Your details added successfully')
            return redirect('home')
        else:
            messages.error(request, 'Error adding your details')
    ctx = {'form': form}
    return render(request, 'gallery/snippet.html', ctx)

def view_category(request, id):
    cat = category.objects.get(id=id)
    snippets = snippet.objects.filter(category=cat)
    ctx = {'cat': cat, 'snippets': snippets}
    return render(request, 'gallery/category.html', ctx)

def view_snippet(request, id):
    snippet = snippet.objects.get(id=id)
    ctx = {'snippet': snippet}
    return render(request, 'gallery/snippet.html', ctx)

def edit_category(request, id):
    cat = category.objects.get(id=id)
    form = categoryForm(request.POST or None, request.FILES or None, instance=cat)
    if request.method == 'POST':
        if form.is_valid():
            form.save() # save the form data to model
            messages.success(request, 'Your details added successfully')
            return redirect('home')
        else:
            messages.error(request, 'Error adding your details')
    ctx = {'form': form}
    return render(request, 'gallery/category.html', ctx)

def edit_snippet(request, id):
    snippet = snippet.objects.get(id=id)
    form = snippetForm(request.POST or None, request.FILES or None, instance=snippet)
    if request.method == 'POST':
        if form.is_valid():
            form.save() # save the form data to model
            messages.success(request, 'Your details added successfully')
            return redirect('home')
        else:
            messages.error(request, 'Error adding your details')
    ctx = {'form': form}
    return render(request, 'gallery/snippet.html', ctx)


def delete_category(request, id):
    cat = category.objects.get(id=id)
    cat.delete()
    messages.success(request, 'Your details added successfully')
    return redirect('home')

def delete_snippet(request, id):
    snippet = snippet.objects.get(id=id)
    snippet.delete()
    messages.success(request, 'Your details added successfully')
    return redirect('home')

