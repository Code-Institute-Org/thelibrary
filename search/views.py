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
        """
        Checks if keywords specifying the course is in search query.
        If True, strips these keywords out of the query and filters
        results for course specified.
        """

        q = self.request.GET.get('q')

        if not any(course in q.lower() for course in ['4p', '5p']):
            q = q.lower().replace('4p', '').replace('5p', '')
            queryset = Post.objects.filter(
                Q(title__icontains=q)
                | Q(summary__icontains=q)
                | Q(body__icontains=q),
                status="Published")
        else:
            course = '1' if '4p' in q.lower() else '2'
            q = q.lower().replace('4p', '').replace('5p', '')
            queryset = Post.objects.filter(
                Q(title__icontains=q)
                | Q(summary__icontains=q)
                | Q(body__icontains=q),
                status="Published", course=course)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context

