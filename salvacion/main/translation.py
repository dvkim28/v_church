from modeltranslation.translator import translator, TranslationOptions
from .models import Article

class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description','description')

translator.register(Article, NewsTranslationOptions)