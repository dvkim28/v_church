from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .models import Article, Feedback
from .forms import ContactForm


class HomeViewForm(FormView):
    template_name = 'main/index.html'
    form_class = ContactForm
    success_url = "/"
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'main/post.html'

