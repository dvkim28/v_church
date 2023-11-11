from django.urls import path
from django.conf import settings
from . import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import HomeViewForm, ArticleDetailView

urlpatterns = [
    path('', HomeViewForm.as_view(), name='homepage'),
    path('news/<slug:slug>/', ArticleDetailView.as_view(), name='post_view'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)