from django import template

from main.models import Article

register = template.Library()

@register.inclusion_tag('main/base/list_news_tag.html')
def show_news_list():
    articles = Article.objects.all().order_by('-id')
    return {'articles': articles}