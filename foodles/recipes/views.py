import logging

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from foodles.recipes.models import Recipe


def home(request):
    return render(request, "recipes/home.html")


@csrf_exempt
def add_recipe(request):
    if request.method.lower() == "post":
        recipe = Recipe(
            title=request.POST["title"],
            ingredients=request.POST["ingredients"],
            quantities=request.POST["quantities"],
            method=request.POST["method"]
        )
        recipe.save()
    return render(request, "recipes/add-recipe.html")
