from .models import PostCategory

def categories(request):
    """ Generates categories for navbar on every page """
    return {'categories_nav': PostCategory.objects.all().order_by('name')}