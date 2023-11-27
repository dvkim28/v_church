from django import template

register = template.Library()

LANGUAGE_TO_FLAG_MAP = {
    'uk': 'ua',  # Украинский
    'ru': 'ru',  # Русский
    'es': 'es',  # Испанский
}

@register.filter
def language_to_flag(lang_code):
    return LANGUAGE_TO_FLAG_MAP.get(lang_code, 'us')  # 'us' - флаг по умолчанию
