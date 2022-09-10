from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
    """
    Class to create the categories model.
    """
    class Meta:
        verbose_name_plural = 'Categories'
    title = models.CharField(max_length=20)
    category_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.title

    def set_slug(self):
        """Sets the slug"""
        return reverse('category', args=[self.title.slug])


class Recipe(models.Model):
    """
    Class to create the recipe model.
    """
    recipe_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    categories = models.ManyToManyField(Category)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipe_post")
    description = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    instructions = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='recipe_like', blank=True)
    featured = models.BooleanField()
    time_taken = models.IntegerField(default=0)
    rating = models.PositiveIntegerField(
        default=3,
        validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        ordering = ['-rating']

    def __str__(self):
        return self.recipe_name

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """
    Class to create the comments model.
    """
    post = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comment_post")
    content = models.TextField()
    approved = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["timestamp"]

    def __str__(self):
        return f"Comment {self.content} by {self.author}"

    def set_slug(self):
        """Sets the slug"""
        return reverse('recipe_detail', args=[self.post.slug])
