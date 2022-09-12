"""
Views to create the webpage from the model and HTML templates
"""
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import View
from django.views import generic
from django.views.generic import UpdateView
from .models import Recipe, Comment
from .forms import CommentForm


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
    categories_list = Recipe.objects.filter(
        categories__title__contains=cats, status=1)
    paginator = Paginator(categories_list, 6)

    page_number = request.GET.get('page')
    categories_list = paginator.get_page(page_number)

    return render(request, 'category.html', {
        'cats': cats.title(), 'categories_list': categories_list})


class Featured(generic.ListView):
    """
    Renders the Featured model for the home page.
    """
    model = Recipe
    queryset = Recipe.objects.filter(featured=True).order_by('-rating')
    template_name = 'index.html'
    paginate_by = 6


class RecipeList(generic.ListView):
    """
    Renders the Recipe List model recipes page and category page.
    """
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-rating')
    template_name = 'recipes.html'
    paginate_by = 6


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
            messages.success(request, """
            Your comment was sent successfully and is awaiting approval!""")
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
def account_view(request):
    """
    Takes users to their account page when signed in
    """
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)

    context = {
        'user_form': user_form,
    }
    return render(request, 'account.html', context)
