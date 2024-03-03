from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'instructions', 'img', 'time_of_execution']  # Include the new field
        widgets = {
            'instructions': forms.Textarea(attrs={'rows': 4}),
            
        }