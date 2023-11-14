from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .models import Article, Feedback
from .forms import ContactForm
from django.contrib import messages
from django.shortcuts import render

class HomeViewForm(FormView):
    template_name = 'main/index.html'
    form_class = ContactForm
    success_url = "/"
    success_message = "City was successfully created"
    def form_valid(self, form):
        form.save()
        # Use self.request to access the request object
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'main/post.html'

class AllNewsView(ListView):
    template_name = 'main/list_view.html'
    model = Article
    context_object_name = 'articles'
    paginate_by = 5

    def get_queryset(self):
        return Article.objects.all().order_by('-id')
