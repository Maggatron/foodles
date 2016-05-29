from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["title", "ingredients", "quantities", "method"]
    ingredients = forms.CharField(widget=forms.Textarea)
    quantities = forms.CharField(widget=forms.Textarea)

class DeleteRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = []
