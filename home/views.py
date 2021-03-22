from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    """
    Render home page
    """
    return render(request, 'index.html')