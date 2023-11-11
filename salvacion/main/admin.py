from django.contrib import admin
from .models import Article, Feedback

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'description']
    # Дополнительные настройки админ-класса для модели Article

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'message', 'date')
    # Дополнительные настройки админ-класса для модели Feedback

admin.site.register(Article, ArticleAdmin)
admin.site.register(Feedback, FeedbackAdmin)
