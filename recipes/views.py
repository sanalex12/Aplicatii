from django.shortcuts import render, redirect, get_object_or_404
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework.permissions import IsAuthenticated






@login_required
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            return redirect('profile')  
    else:
        form = RecipeForm()
    return render(request, 'recipes/create_recipe.html', {'form': form})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

@login_required
def update_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, user=request.user)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('profile')  
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/update_recipe.html', {'form': form, 'recipe': recipe})

@login_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, user=request.user)
    if request.method == 'POST':
        recipe.delete()
        return redirect('profile')  
    return render(request, 'recipes/delete_recipe.html', {'recipe': recipe})


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (IsAuthenticated, )
