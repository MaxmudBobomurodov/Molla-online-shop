from django.views.generic import ListView, TemplateView
from blogs.models import BlogModel, BlogCategory

class BlogListView(ListView):
    model = BlogModel
    template_name = 'blogs/blogs.html'
    context_object_name = 'blogs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = BlogCategory.objects.all()
        return context

class BlogDetailView(TemplateView):
    template_name = 'blogs/blog-detail.html'