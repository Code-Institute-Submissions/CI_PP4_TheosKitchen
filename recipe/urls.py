"""
URL path patterns
"""
from django.urls import path
from . import views


urlpatterns = [
     path('', views.Featured.as_view(), name="Home"),
     path('add_recipe', views.add_recipe_, name="add_recipe"),
     path('edit_recipe/<slug:slug>', views.edit_recipe, name="edit_recipe"),
     path('delete/<slug:slug>', views.delete_recipe, name='delete'),
     path('profile/', views.profile_, name="profile"),
     path('categories/', views.categories, name="categories"),
     path('categories_list/<str:cats>', views.categories_view,
          name="categories_list"),
     path('recipes/', views.RecipeList.as_view(), name="recipes"),
     path('<slug:slug>/', views.RecipeDetail.as_view(), name="recipe_detail"),
     path('like/<slug:slug>/', views.RecipeLike.as_view(), name="recipe_like"),
     path('delete_comment/<int:comment_id>', views.delete_comment,
          name="delete_comment"),
     path('edit_comment/<int:pk>', views.EditComment.as_view(),
          name="edit_comment"),
]
