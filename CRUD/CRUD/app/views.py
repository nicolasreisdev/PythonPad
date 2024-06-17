from django.shortcuts import render, redirect
from app.forms import CarrosForm
from app.models import Carros
# Create your views here.

def home(request):
    data = {}
    data['db'] = Carros.objects.all() # get all the data from the Carros table
    return render(request, 'index.html', data) # render the index.html template

def form(request):
    data = {}
    data['form'] = CarrosForm() # create the form object  
    return render(request, 'form.html', data) # render the form.html template

def create(request):
    form = CarrosForm(request.POST or None) # create the form object
    if form.is_valid(): # check if the form is valid
        form.save() # save the form
        form = CarrosForm() # create a new form object
        return redirect('home') # redirect to the home view
    
def view(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk) # get the data from the Carros table
    return render(request, 'view.html', data) # render the view.html template

def edit(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk) # get the data from the Carros table
    data['form'] = CarrosForm(instance=data['db']) # create the form object
    return render(request, 'form.html', data) # render the form.html template

def update(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk) # get the data from the Carros table
    form = CarrosForm(request.POST or None, instance=data['db']) # create the form object
    if form.is_valid(): # check if the form is valid
        form.save() # save the form
        return redirect('home') # redirect to the home view
    
def delete(request, pk):
    db = Carros.objects.get(pk=pk) # get the data from the Carros table
    db.delete() # delete the data
    return redirect('home') # redirect to the home view