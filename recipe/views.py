from django.shortcuts import render
from django.views import generic
from .models import Recipe


def categories(request):
    return render(request, 'categories.html')


def error_500(request):
    data = {}
    return render(request, '500.html', data)


def categories_view(request, cats):
    """
    Renders the recipes filtered by categories
    """
    categories_list = Recipe.objects.filter(
        categories__title__contains=cats, status=1)
    return render(request, 'category.html', {
        'cats': cats.title(), 'categories_list': categories_list})


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
