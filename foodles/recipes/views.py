import logging

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

from .models import Recipe
from .forms import RecipeForm, DeleteRecipeForm

def home(request):
    all_recipes = Recipe.objects.all()
    return render(request, "recipes/home.html", {"all_recipes":all_recipes})


@csrf_exempt
def edit_recipe(request, id=None):
    recipe = None
    if id:
        recipe = Recipe.objects.get(pk=int(id))

    if request.method.lower() == "post":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            recipe = form.save()
            return HttpResponseRedirect('/')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, "recipes/edit-recipe.html", {'form':form})

@csrf_exempt
def delete_recipe(request, id=None):
    recipe = Recipe.objects.get(pk=int(id))
    if request.method.lower() == "post":
        form = DeleteRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            recipe.delete()
            return HttpResponseRedirect('/')
    else:
        form = DeleteRecipeForm(instance=recipe)
    return render(request, "recipes/delete-recipe.html", {'form':form})
