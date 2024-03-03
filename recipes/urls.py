from django.urls import path
from .views import create_recipe,recipe_detail,update_recipe,delete_recipe


urlpatterns = [
    path('create/', create_recipe, name='create_recipe'),
    path('recipe/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
    path('update/<int:recipe_id>/', update_recipe, name='update_recipe'),
    path('delete/<int:recipe_id>/', delete_recipe, name='delete_recipe'),
]