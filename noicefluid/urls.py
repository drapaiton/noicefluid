# imgs
from django.conf.urls.static import static
from django.conf import settings
# path
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('', include('lobby.urls')),
    path('chat/', include('chat.urls')),
    path('admin/', admin.site.urls),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
