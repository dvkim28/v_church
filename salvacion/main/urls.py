from django.urls import path
from django.conf import settings
from . import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import HomeViewForm, ArticleDetailView, AllNewsView, HistoryView

urlpatterns = [
    path('', HomeViewForm.as_view(), name='homepage'),
    path('history/', HistoryView, name='history'),  # Assuming HistoryView is a class-based view
    path('news/<slug:slug>/', ArticleDetailView.as_view(), name='post_view'),
    path('news/', AllNewsView.as_view(), name='list_view'),
    path('contact/', AllNewsView.as_view(), name='contacts'),
]

# Static files and media files URL patterns
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
