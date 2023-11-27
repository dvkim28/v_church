from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Article, Feedback

class ArticleAdmin(TranslationAdmin):
    list_display = ['title', 'slug', 'short_description', 'description']

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # Здесь вы можете добавить логику для исключения полей для испанского языка
        for field in ['title_es', 'slug_es', 'short_description_es', 'description_es']:
            if field in form.base_fields:
                form.base_fields.pop(field)
        return form

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'message', 'date')
    # Дополнительные настройки админ-класса для модели Feedback

admin.site.register(Article, ArticleAdmin)
admin.site.register(Feedback, FeedbackAdmin)
