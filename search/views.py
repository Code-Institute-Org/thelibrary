from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView

from posts.models import Post


class SearchResultsView(LoginRequiredMixin, ListView):
    """ Render search results with pagination """
    template_name = "search/search_results.html"
    paginate_by = 12
    context_object_name = 'posts'

    def get_queryset(self):

        q = self.request.GET.get('q')
        print(q)

        if '4P' not in q and '5P' not in q:
            queryset = Post.objects.filter(
                Q(title__icontains=q)
                | Q(summary__icontains=q)
                | Q(body__icontains=q),
                status="Published")
        elif '4P' in q:
            queryset = Post.objects.filter(
                Q(title__icontains=q)
                | Q(summary__icontains=q)
                | Q(body__icontains=q),
                status="Published", course='1')
        else:
            queryset = Post.objects.filter(
                Q(title__icontains=q)
                | Q(summary__icontains=q)
                | Q(body__icontains=q),
                status="Published", course='1')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context
