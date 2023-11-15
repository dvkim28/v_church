from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .models import Article, Feedback
from .forms import ContactForm
from django.contrib import messages
from django.shortcuts import render

from .utils import send_telegram_bot


class HomeViewForm(FormView):
    template_name = 'main/index.html'
    form_class = ContactForm
    success_url = "/"
    success_message = "Ваше повідомлення успішно надіслано до церкви"
    def form_valid(self, form):
        form.save()
        feedback_instance = form.save()
        name = feedback_instance.name
        number = feedback_instance.number
        message = feedback_instance.message
        full_message = f"Нове повідомлення:\nІмʼя: {name}\nНомер: {number}\nПовідомлення: {message}"
        send_telegram_bot(full_message)
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
