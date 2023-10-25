from django.urls import path
from .views import handle_user_input
from django.conf.urls.static import static
from django.conf import settings

app_name = 'classifier'

urlpatterns = [
    path('user_input/', handle_user_input, name='user_input'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)