import logging

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

from .models import Recipe
from .forms import RecipeForm

def home(request):
    all_recipes = Recipe.objects.all()
    return render(request, "recipes/home.html", {"all_recipes":all_recipes})


@csrf_exempt
def add_recipe(request):
    if request.method.lower() == "post":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = Recipe(**form.cleaned_data)
            recipe.save()
            return HttpResponseRedirect('/')
    else:
        form = RecipeForm()
    return render(request, "recipes/add-recipe.html", {'form':form})
