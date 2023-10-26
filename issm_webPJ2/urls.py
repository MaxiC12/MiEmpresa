
#from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Personas2.urls')),
    path('', include('Personas2.urls')), 
    path('accounts/',include('django.contrib.auth.urls')),
]

urlpatterns+= staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
