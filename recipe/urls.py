from . import views
from django.urls import path


urlpatterns = [
    path('', views.Featured.as_view(), name="Home"),
    path('recipes/', views.RecipeList.as_view(), name="recipes"),
    path('categories/', views.categories, name="categories"),
    path('categories_list/<str:cats>', views.categories,
         name="categories_posts"),
]
