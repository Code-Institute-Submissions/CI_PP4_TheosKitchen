from django.urls import path
from .forms import CommentForm
from . import views
from .views import *


urlpatterns = [
     path('', views.Featured.as_view(), name="Home"),
     path('recipes/', views.RecipeList.as_view(), name="recipes"),
     path('categories/', views.categories, name="categories"),
     path('categories_list/<str:cats>', views.categories_view,
          name="categories_list"),
     path('<slug:slug>/', views.RecipeDetail.as_view(), name="recipe_detail"),
     path('like/<slug:slug>/', views.RecipeLike.as_view(), name="recipe_like"),
     path('delete_comment/<int:comment_id>', views.delete_comment,
          name="delete_comment"),
     path('edit_comment/<int:pk>', views.EditComment.as_view(),
          name="edit_comment"),
]
