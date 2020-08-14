from django.contrib import admin

from django.urls import path
from django.conf.urls import include

from django.conf.urls.static import static
from django.conf import settings
# favicon
from django.conf.urls import url
from django.http import HttpResponseRedirect
urlpatterns = [
    path('', include('lobby.urls')),
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
    url(r'^favicon.ico/$',
        lambda x: HttpResponseRedirect(settings.STATIC_URL + 'favicon.ico')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
