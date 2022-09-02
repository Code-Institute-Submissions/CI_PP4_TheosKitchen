from django.shortcuts import render
from django.views import generic
from .models import Recipe


def categories(request):
    return render(request, 'categories.html')


class Featured(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(featured=True).order_by('-rating')
    template_name = 'index.html'
    paginate_by = 6


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-rating')
    template_name = 'recipes.html'
    paginate_by = 6
