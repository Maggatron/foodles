from django import forms

class RecipeForm(forms.Form):
    title = forms.CharField(label="title", max_length=100)
    ingredients = forms.CharField(label="ingredients", widget=forms.Textarea)
    quantities = forms.CharField(label="quantities", widget=forms.Textarea)
    method = forms.CharField(label="method", widget=forms.Textarea)
