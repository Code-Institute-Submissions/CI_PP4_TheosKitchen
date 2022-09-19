"""
Views to create the webpage from the model and HTML templates
"""
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import update_session_auth_hash
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.template.defaultfilters import slugify
from django.views import View
from django.views import generic
from django.views.generic import UpdateView
# from django.contrib.auth.forms import PasswordChangeForm
from .models import Recipe, Comment
from .forms import CommentForm, UserUpdateForm, AddEditRecipeForm, MyChangePasswordForm


def categories(request):
    """
    Renders the categories page.
    """
    return render(request, 'categories.html')


def error_500(request):
    data = {}
    return render(request, '500.html', data)


def categories_view(request, cats):
    """
    Renders the recipes filtered by categories.
    """
    category = Recipe.objects.filter(
        categories__title__contains=cats, status=1)

    paginator = Paginator(category, 6)

    page_number = request.GET.get('page')
    category = paginator.get_page(page_number)

    return render(request, 'category.html', {
        'cats': cats.title(), 'category': category})


class Featured(generic.ListView):
    """
    Renders the Featured model for the home page.
    """
    model = Recipe
    queryset = Recipe.objects.filter(featured=True).order_by('-rating')
    template_name = 'index.html'
    paginate_by = 8


class RecipeList(generic.ListView):
    """
    Renders the Recipe List model recipes page and category page.
    """
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-rating')
    template_name = 'recipes.html'
    paginate_by = 8


class RecipeDetail(View):
    """
    Renders the RecipeDetail model for the recipe_detail page.
    """
    def get(self, request, slug):
        queryset = Recipe.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-timestamp")
        number_comments = Comment.objects.filter(post=post).count()
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(request, "recipe_detail.html", {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
                'number_comments': number_comments,
            },
        )

    def post(self, request, slug):
        """
        Comment on the posts
        """
        queryset = Recipe.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-timestamp")
        liked = False

        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.author = request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(
                request,
                """Your comment was sent successfully and is awaiting approval!""")
        else:
            comment_form = CommentForm()
        return render(
            request,
            "recipe_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked,
            },
        )


@login_required
def delete_comment(request, comment_id):
    """
    Delete user Comments from recipes
    """
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    messages.success(request, 'The comment was deleted successfully')
    return HttpResponseRedirect(reverse(
        'recipe_detail', args=[comment.post.slug]))


class RecipeLike(LoginRequiredMixin, View):
    """
    Allows users to Like and and unlike Recipes
    """
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Recipe, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            messages.success(request, 'You have unliked this post.')
        else:
            post.likes.add(request.user)
            messages.success(request, 'You have liked this post, thanks!')
        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


class EditComment(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
     Allow users to edit their comments.
    """
    model = Comment
    template_name = 'edit_comment.html'
    form_class = CommentForm
    success_message = 'The comment was successfully updated'


@login_required
def profile_(request):
    """
    Takes users to their profile page when signed in
    """
    user = request.user
    favorites = Recipe.objects.filter(likes=user)
    personal_recipes = Recipe.objects.filter(author=user)
    user_form = UserUpdateForm(request.POST or None, instance=user)
    password_change_form = MyChangePasswordForm(user, data=request.POST)
    if request.method == 'POST':
        if 'user_' in request.POST:
            if user_form.is_valid():
                user_form.save()
                messages.success(request, 'Your profile has been updated!')
                return redirect('profile')
            else:
                messages.error(
                    request, 'Your profile could not be updated at this time.')

        elif 'password_' in request.POST:
            if password_change_form.is_valid():
                password_change_form.save()
                update_session_auth_hash(request, password_change_form.user)
                messages.success(request, 'Your password has been updated!')
                return redirect('profile')
            else:
                password_change_form = MyChangePasswordForm(user, data=request.POST)
                messages.error(
                    request, 'your password could not be updated at this time')

    context = {'user_form': user_form,
               'password_change_form': password_change_form,
               'favorites': favorites,
               'personal_recipes': personal_recipes,
               }

    return render(request, 'profile.html', context)


def add_recipe_(request):
    """
    Adds a new user recipe to the website.
    """
    recipe_form = AddEditRecipeForm(request.POST)
    if request.method == 'POST':
        if recipe_form.is_valid():
            new_recipe = recipe_form.save(commit=False)
            new_recipe.author = request.user
            new_recipe.status = 1
            new_recipe.slug = slugify(new_recipe.recipe_name)
            new_recipe = recipe_form.save()
            return redirect('profile')
    context = {'recipe_form': recipe_form}

    return render(request, 'add_recipes.html', context)


def edit_recipe(request, slug):
    """
    Edits a user recipe on the website.
    """
    recipe = get_object_or_404(Recipe, slug=slug)
    if request.method == 'POST':
        recipe_form = AddEditRecipeForm(request.POST, instance=recipe)
        if recipe_form.is_valid():
            recipe_form.save()
            return redirect('profile')
    recipe_form = AddEditRecipeForm(instance=recipe)
    context = {'recipe_form': recipe_form}

    return render(request, 'edit_recipes.html', context)


def delete_recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    recipe.delete()
    return redirect('profile')
