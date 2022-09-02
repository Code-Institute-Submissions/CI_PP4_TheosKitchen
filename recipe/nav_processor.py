from .models import *


def catslist(request):
    """
    Processes the catagories into a list.
    """
    categories = Category.objects.all()
    context = {
        'categories_list': categories
    }

    return context
