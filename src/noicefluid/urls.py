from django.contrib import admin

from django.urls import path
from django.conf.urls import include

from django.conf.urls.static import static
from django.conf import settings
# favicon
from django.conf.urls import url
from django.http import HttpResponseRedirect
from django.http import HttpResponse


def read_file(request):
    f = open('.well-known/pki-validation/99D5CBF06D40378C8C8BE2B0118D19B7.txt', 'r')
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type="text/plain")


urlpatterns = [
    path('', include('lobby.urls')),
    url(r'^.well-known/pki-validation/99D5CBF06D40378C8C8BE2B0118D19B7.txt$', lambda x: HttpResponseRedirect(
        settings.STATIC_URL + '99D5CBF06D40378C8C8BE2B0118D19B7.txt')),
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
    url(r'^favicon.ico/$',
        lambda x: HttpResponseRedirect(settings.STATIC_URL + 'favicon.ico')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
